"""Worst Fix Ever: Funniest Commit Message (make.fun).

One fixed commit message, 94 characters, for a bug fix that made
everything worse. The program writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline, so the
file holds exactly the line itself. Standard library only, fully
deterministic: the same line every run.

The joke: the hotfix "worked" — no more crashes — because the
catch-all swallowed every exception, so nothing runs at all. The
fix succeeded on its own metric and destroyed what it repaired.
"""

import os
from pathlib import Path

ENTRY = (
    "fix: hotfixed the crash by catching every exception; "
    "nothing crashes now, nothing works either"
)

# The sealed gate counts 1 to 100 characters; stay one short of the
# ceiling so an off-by-one in the gate's counting cannot fail us.
MAX_CHARS = 99


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
