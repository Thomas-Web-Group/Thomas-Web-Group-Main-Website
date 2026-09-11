from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "assets" / "img"

EXTENSIONS = {".html", ".css", ".js", ".json", ".njk", ".md"}
SKIP_DIRS = {".git", "node_modules", "_site", ".venv"}
APPLY = "--apply" in sys.argv

# Match quoted strings. No nested or ambiguous repetition.
QUOTED = re.compile(r"""(["'])(.*?)\1""", re.DOTALL)

# Match unquoted CSS url(...) paths.
CSS_URL = re.compile(r"url\(\s*([^'\"\s)][^)]*?)\s*\)", re.IGNORECASE)

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}

def convert_reference(value, source_file):
    value = value.strip()

    # Split off query strings and fragments.
    parts = urlsplit(value)

    if parts.scheme or parts.netloc:
        return None

    path = unquote(parts.path)

    if Path(path).suffix.lower() not in IMAGE_SUFFIXES:
        return None

    if path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = source_file.parent / path

        if not target.is_file():
            target = ROOT / path

    if not target.is_file():
        return None

    try:
        target.relative_to(IMAGE_DIR)
    except ValueError:
        return None

    webp = target.with_suffix(".webp")

    if not webp.is_file():
        return None

    new_path = str(Path(parts.path).with_suffix(".webp")).replace("\\", "/")

    return new_path + (f"?{parts.query}" if parts.query else "") + (f"#{parts.fragment}" if parts.fragment else "")

total = 0

for file_path in ROOT.rglob("*"):
    if not file_path.is_file():
        continue

    if any(part in SKIP_DIRS for part in file_path.relative_to(ROOT).parts):
        continue

    if file_path.suffix.lower() not in EXTENSIONS:
        continue

    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    changes = []

    def replace_quoted(match):
        quote, value = match.groups()
        new_value = convert_reference(value, file_path)

        if new_value is None:
            return match.group(0)

        changes.append((value, new_value))
        return quote + new_value + quote

    updated = QUOTED.sub(replace_quoted, text)

    # Handle CSS url(path.jpg) without quotes.
    def replace_css(match):
        value = match.group(1).strip()
        new_value = convert_reference(value, file_path)

        if new_value is None:
            return match.group(0)

        changes.append((value, new_value))
        return f"url({new_value})"

    updated = CSS_URL.sub(replace_css, updated)

    if changes:
        print(f"\n{file_path.relative_to(ROOT)}", flush=True)

        for old, new in changes:
            print(f"  {old} -> {new}", flush=True)

        total += len(changes)

        if APPLY:
            file_path.write_text(updated, encoding="utf-8")

print(f"\n{total} references found.")
print("Changes applied." if APPLY else "DRY RUN - no files changed.")