#!/usr/bin/env python3
"""Validate and lightly sanitize short funny titles."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_SENSITIVE_WORDS = [
    "哈哈哈",
    "哈哈",
    "笑死",
    "救命",
    "谁懂啊",
    "绝了",
    "傻逼",
    "弱智",
    "脑残",
    "死全家",
    "丑逼",
    "肥猪",
]

EMOJI_RE = re.compile(
    "["
    "\U0001F1E6-\U0001F1FF"
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\u2600-\u27BF"
    "]",
    flags=re.UNICODE,
)
VARIATION_SELECTOR_RE = re.compile("[\ufe0e\ufe0f]")
ZERO_WIDTH_JOINER = "\u200d"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Remi-style funny titles: <=20 chars, no sensitive words, <=3 emoji."
    )
    parser.add_argument("titles", nargs="*", help="Titles to validate.")
    parser.add_argument("--input", "-i", help="Text file with one title per line.")
    parser.add_argument("--max-chars", type=int, default=20, help="Maximum visible characters.")
    parser.add_argument("--max-emoji", type=int, default=3, help="Maximum emoji count.")
    parser.add_argument(
        "--sensitive-words",
        default="",
        help="Comma-separated extra sensitive words to remove.",
    )
    parser.add_argument(
        "--sensitive-file",
        help="Text file with one extra sensitive word per line.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    return parser.parse_args()


def load_titles(args: argparse.Namespace) -> list[str]:
    titles: list[str] = []
    if args.input:
        titles.extend(Path(args.input).read_text(encoding="utf-8").splitlines())
    if args.titles:
        titles.extend(args.titles)
    if not titles and not sys.stdin.isatty():
        titles.extend(sys.stdin.read().splitlines())
    return [title.strip() for title in titles if title.strip()]


def load_sensitive_words(args: argparse.Namespace) -> list[str]:
    words = list(DEFAULT_SENSITIVE_WORDS)
    if args.sensitive_words:
        words.extend(word.strip() for word in args.sensitive_words.split(",") if word.strip())
    if args.sensitive_file:
        words.extend(
            word.strip()
            for word in Path(args.sensitive_file).read_text(encoding="utf-8").splitlines()
            if word.strip() and not word.lstrip().startswith("#")
        )
    return sorted(set(words), key=len, reverse=True)


def visible_chars(title: str) -> list[str]:
    chars = []
    for char in title:
        if char.isspace():
            continue
        if char == ZERO_WIDTH_JOINER or VARIATION_SELECTOR_RE.fullmatch(char):
            continue
        chars.append(char)
    return chars


def emoji_count(title: str) -> int:
    return len(EMOJI_RE.findall(title))


def trim_emoji(title: str, max_emoji: int) -> str:
    kept = 0
    output = []
    for char in title:
        if EMOJI_RE.fullmatch(char):
            kept += 1
            if kept > max_emoji:
                continue
        output.append(char)
    return "".join(output)


def sanitize(title: str, sensitive_words: list[str], max_emoji: int) -> tuple[str, list[str]]:
    removed_words = []
    result = title.strip()
    for word in sensitive_words:
        if word in result:
            result = result.replace(word, "")
            removed_words.append(word)
    result = trim_emoji(result, max_emoji)
    result = re.sub(r"\s+", " ", result).strip()
    return result, removed_words


def validate_title(
    title: str,
    sensitive_words: list[str],
    max_chars: int,
    max_emoji: int,
) -> dict[str, object]:
    sanitized, removed_words = sanitize(title, sensitive_words, max_emoji)
    original_length = len(visible_chars(title))
    original_emojis = emoji_count(title)
    length = len(visible_chars(sanitized))
    emojis = emoji_count(sanitized)
    issues = []
    if original_length > max_chars:
        issues.append(f"original_over_{max_chars}_chars")
    if length > max_chars:
        issues.append(f"sanitized_over_{max_chars}_chars")
    if original_emojis > max_emoji:
        issues.append(f"original_over_{max_emoji}_emoji")
    if removed_words:
        issues.append("sensitive_words_removed")
    if not sanitized:
        issues.append("empty_after_sanitize")
    return {
        "original": title,
        "sanitized": sanitized,
        "originalChars": original_length,
        "originalEmoji": original_emojis,
        "chars": length,
        "emoji": emojis,
        "removedSensitiveWords": removed_words,
        "sanitizedOk": length <= max_chars and emojis <= max_emoji and bool(sanitized),
        "ok": not issues,
        "issues": issues,
    }


def render_text(results: list[dict[str, object]]) -> str:
    lines = []
    for result in results:
        status = "OK" if result["ok"] else "FIX"
        issues = ", ".join(result["issues"]) if result["issues"] else "-"
        lines.append(
            f"[{status}] {result['sanitized']} "
            f"(chars={result['chars']}, emoji={result['emoji']}, issues={issues})"
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    titles = load_titles(args)
    if not titles:
        print("No titles provided. Pass titles as args, --input, or stdin.", file=sys.stderr)
        return 2

    sensitive_words = load_sensitive_words(args)
    results = [
        validate_title(title, sensitive_words, args.max_chars, args.max_emoji)
        for title in titles
    ]

    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(render_text(results))
    return 1 if any(not result["ok"] for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
