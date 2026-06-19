#!/usr/bin/env python3
"""Convert PGMM.txt (PDF extract) to structured Markdown."""

import re
import sys
from pathlib import Path

COPYRIGHT = re.compile(r"©\s*О\.Е\.\s*Клепиков\s*2025\s*")
SPLIT_MARKERS = re.compile(
    r"(ЧАСТЬ\s+[IVX]+\.\s+[^©]+|ПРИЛОЖЕНИЕ\s+[A-E]\.\s+[^©]+)"
)
PART = re.compile(r"^(?:ЧАСТЬ|ПРИЛОЖЕНИЕ)\s+([IVX]+|[A-E])\.\s*(.+)$", re.IGNORECASE)
ROMAN_SECTION = re.compile(r"^([IVX]+)\.([0-9]+(?:\.[0-9]+)*)\.\s*(.+)$")
APP_SECTION = re.compile(r"^([A-E])\.([0-9]+(?:\.[0-9]+)*)\.\s*(.+)$")
STEP_SECTION = re.compile(r"^([0-9]+)\.\s+Шаг\s+(.+)$")
NUM_SECTION = re.compile(r"^([0-9]+(?:\.[0-9]+)*)\.\s*(.+)$")
BULLET_TOP = re.compile(r"^•\s*(.*)$")
BULLET_SUB = re.compile(r"^o\s+(.*)$", re.IGNORECASE)
BULLET_DEEP = re.compile(r"^▪\s*(.*)$")
INLINE_BULLET = re.compile(r"\s•\s+")
HEADING_END = re.compile(r"[.!?;:)\]}»\"]$")
LOWER_START = re.compile(r"^[a-zа-яё0-9(,«\"']")
JSON_START = re.compile(r"^\s*\{\s*\"")
JSON_LINE = re.compile(r'^\s*"[A-Z_]+"\s*:')


def clean_line(line: str) -> str:
    line = COPYRIGHT.sub("\n", line)
    line = re.sub(r"\s+", " ", line).strip()
    # PDF line-break artifacts inside words
    line = re.sub(r"ПРИЛОЖЕНИ\s+Е", "ПРИЛОЖЕНИЕ", line, flags=re.IGNORECASE)
    line = re.sub(r"МЕТАСПЕЦИФИКАЦ\s+ИЯ", "МЕТАСПЕЦИФИКАЦИЯ", line, flags=re.IGNORECASE)
    line = re.sub(r"\s+-\s+", "-", line)
    line = re.sub(r"\s+–\s+", " – ", line)
    return line


def preprocess(raw_lines: list[str]) -> list[str]:
    out: list[str] = []
    for raw in raw_lines:
        line = clean_line(raw)
        if not line:
            out.append("")
            continue
        parts = SPLIT_MARKERS.split(line)
        for part in parts:
            part = part.strip()
            if part:
                out.append(part)
    return out


def is_heading_candidate(text: str) -> bool:
    if PART.match(text):
        return True
    if ROMAN_SECTION.match(text):
        return True
    if APP_SECTION.match(text):
        return True
    if STEP_SECTION.match(text):
        return True
    m = NUM_SECTION.match(text)
    if not m:
        return False
    nums = m.group(1).split(".")
    body = m.group(2)
    if STEP_SECTION.match(text):
        return True
    if len(nums) == 1 and body.startswith("Шаг "):
        return True
    if len(nums) == 1 and int(nums[0]) <= 20 and len(body) < 100:
        return True
    if len(nums) <= 3 and len(body) < 120 and not body.startswith("S") and body[0].isupper():
        return True
    return False


def heading_level(text: str) -> int:
    if PART.match(text):
        return 2
    if STEP_SECTION.match(text):
        return 3
    m = ROMAN_SECTION.match(text)
    if m:
        return min(3 + m.group(2).count("."), 5)
    m = APP_SECTION.match(text)
    if m:
        return min(3 + m.group(2).count("."), 5)
    m = NUM_SECTION.match(text)
    if m:
        if m.group(2).startswith("Шаг "):
            return 3
        return min(3 + m.group(1).count("."), 5)
    return 3


def should_join(prev: str, nxt: str) -> bool:
    if not prev or not nxt:
        return False
    if is_heading_candidate(nxt):
        return False
    if BULLET_TOP.match(nxt) or BULLET_SUB.match(nxt) or BULLET_DEEP.match(nxt):
        return False
    if NUM_SECTION.match(nxt) and is_heading_candidate(nxt):
        return False
    if prev.startswith("{") or nxt.startswith("{"):
        return False
    if JSON_START.match(nxt) or JSON_LINE.match(nxt):
        return False
    if HEADING_END.search(prev):
        return False
    if LOWER_START.match(nxt):
        return True
    if prev.endswith("-") or prev.endswith(","):
        return True
    return False


def join_paragraphs(lines: list[str]) -> list[str]:
    out: list[str] = []
    buf = ""
    for line in lines:
        if not line:
            if buf:
                out.append(buf)
                buf = ""
            out.append("")
            continue
        if buf and should_join(buf, line):
            if buf.endswith("-"):
                buf = buf[:-1] + line
            else:
                buf = buf + " " + line
        else:
            if buf:
                out.append(buf)
            buf = line
    if buf:
        out.append(buf)
    return out


def split_inline_bullets(text: str) -> list[str]:
    if "•" not in text:
        return [text]
    parts = INLINE_BULLET.split(text)
    result = [parts[0].strip()] if parts[0].strip() else []
    for p in parts[1:]:
        p = p.strip()
        if p:
            result.append("• " + p)
    return result


def format_bullet_line(text: str):
    m = BULLET_DEEP.match(text)
    if m:
        return "      - " + m.group(1)
    m = BULLET_SUB.match(text)
    if m:
        return "    - " + m.group(1)
    m = BULLET_TOP.match(text)
    if m:
        return "- " + m.group(1)
    return None


def is_json_block_start(text: str) -> bool:
    return bool(JSON_START.match(text))


def convert(lines: list[str]) -> str:
    pre = preprocess(lines)
    joined = join_paragraphs(pre)
    md: list[str] = []
    title_done = False
    json_mode = False
    json_buf: list[str] = []

    for line in joined:
        if not line.strip():
            if json_mode:
                json_buf.append("")
            else:
                md.append("")
            continue

        if json_mode:
            json_buf.append(line)
            if re.match(r"^\}\s*$", line.strip()):
                md.append("```json")
                md.extend(json_buf)
                md.append("```")
                md.append("")
                json_mode = False
                json_buf = []
            continue

        if is_json_block_start(line):
            json_mode = True
            json_buf = [line]
            continue

        for chunk in split_inline_bullets(line):
            text = chunk.strip()
            if not text:
                continue

            if not title_done and "(PGMM)" in text and len(text) < 80:
                md.extend(
                    [
                        "# Практическое руководство по метафорическому мэппингу (PGMM)",
                        "",
                        "© О.Е. Клепиков, 2025",
                        "",
                    ]
                )
                title_done = True
                continue

            if not title_done and text == "ПРАКТИЧЕСКОЕ РУКОВОДСТВО ПО МЕТАФОРИЧЕСКОМУ МЭППИНГУ":
                continue

            bullet = format_bullet_line(text)
            if bullet:
                md.append(bullet)
                continue

            if is_heading_candidate(text):
                level = heading_level(text)
                md.append("#" * level + " " + text)
                md.append("")
                continue

            md.append(text)

    if json_mode and json_buf:
        md.append("```json")
        md.extend(json_buf)
        md.append("```")

    result: list[str] = []
    blank = 0
    for line in md:
        if not line.strip():
            blank += 1
            if blank <= 2:
                result.append("")
        else:
            blank = 0
            result.append(line.rstrip())

    body = "\n".join(result).strip() + "\n"

    toc = build_toc(body)
    if toc:
        insert_at = body.find("\n\n## ")
        if insert_at == -1:
            insert_at = body.find("\n\n### ")
        if insert_at != -1:
            body = body[:insert_at] + "\n\n" + toc + body[insert_at:]

    return body


def build_toc(body: str) -> str:
    headings = []
    for line in body.splitlines():
        m = re.match(r"^(#{2,5})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level <= 4 and (
                title.startswith("ЧАСТЬ")
                or title.startswith("ПРИЛОЖЕНИЕ")
                or title.startswith("Шаг")
                or re.match(r"^[0-9IVX]+\.", title)
            ):
                slug = re.sub(r"[^\w\s-]", "", title.lower())
                slug = re.sub(r"\s+", "-", slug.strip())[:80]
                headings.append((level, title, slug))
    if len(headings) < 5:
        return ""

    lines = ["## Оглавление", ""]
    for level, title, slug in headings[:60]:
        indent = "  " * (level - 2)
        lines.append(f"{indent}- [{title}](#{slug})")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "PGMM.txt"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".md")

    text = src.read_text(encoding="utf-8")
    md = convert(text.splitlines())
    dst.write_text(md, encoding="utf-8")
    print(f"Written: {dst} ({len(md):,} chars, {md.count(chr(10)):,} lines)")


if __name__ == "__main__":
    main()
