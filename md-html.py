#!/usr/bin/env python3
"""
md_to_html.py — Convert Jekyll .md posts to .html posts.

Usage:
    # Convert a single file:
    python3 md_to_html.py _posts/2025-06-24-gpedit.md

    # Convert all .md posts in _posts/ (skips templates/howto):
    python3 md_to_html.py --all _posts/

    # Dry run (preview what would be converted):
    python3 md_to_html.py --all _posts/ --dry-run

The script:
  - Extracts YAML front matter and keeps it unchanged
  - Converts Markdown body → HTML using the 'markdown' library
    with tables, fenced code blocks, and code highlighting extensions
  - Writes a new .html file alongside the original
  - Does NOT delete the original .md — do that manually once you've verified
"""

import sys
import re
import argparse
from pathlib import Path
import markdown as md_lib

SKIP_FILES = {"howto.md", "example-post-template.md", "POST-TEMPLATE.md"}

EXTENSIONS = [
    "tables",           # GFM-style tables
    "fenced_code",      # ```lang blocks
    "codehilite",       # syntax highlighting classes
    "nl2br",            # newlines → <br> in paragraphs
    "attr_list",        # {: .class} attribute syntax
    "def_list",
    "footnotes",
    "toc",
]

EXTENSION_CONFIGS = {
    "codehilite": {
        "css_class": "highlight",
        "guess_lang": False,
    }
}


def split_front_matter(text: str) -> tuple[str, str]:
    """Split Jekyll front matter from body. Returns (front_matter_block, body)."""
    match = re.match(r'^(---\n.*?\n---\n)', text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def convert_file(src: Path, dry_run: bool = False) -> Path | None:
    if src.suffix != ".md":
        print(f"  skip (not .md): {src.name}")
        return None
    if src.name in SKIP_FILES:
        print(f"  skip (template): {src.name}")
        return None

    text = src.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text)

    if not front_matter:
        print(f"  WARNING: no front matter found in {src.name}, skipping")
        return None

    # Convert markdown body to HTML
    html_body = md_lib.markdown(
        body,
        extensions=EXTENSIONS,
        extension_configs=EXTENSION_CONFIGS,
    )

    dest = src.with_suffix(".html")
    output = front_matter + html_body + "\n"

    if dry_run:
        print(f"  [dry-run] would write: {dest.name}")
        return dest

    dest.write_text(output, encoding="utf-8")
    print(f"  converted: {src.name} → {dest.name}")
    return dest


def main():
    parser = argparse.ArgumentParser(description="Convert Jekyll .md posts to .html")
    parser.add_argument("target", help="A single .md file, or a directory when using --all")
    parser.add_argument("--all", action="store_true", help="Convert all .md files in directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    target = Path(args.target)

    if args.all:
        if not target.is_dir():
            print(f"Error: {target} is not a directory")
            sys.exit(1)
        files = sorted(target.glob("*.md"))
        print(f"Found {len(files)} .md files in {target}\n")
        for f in files:
            convert_file(f, dry_run=args.dry_run)
    else:
        if not target.exists():
            print(f"Error: {target} does not exist")
            sys.exit(1)
        convert_file(target, dry_run=args.dry_run)

    if not args.dry_run:
        print("\nDone. The original .md files are untouched — delete them manually once verified.")
        print("Or run: rm _posts/*.md  (only after checking the .html output is correct)")


if __name__ == "__main__":
    main()