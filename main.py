"""Fortune Cookie Funnies for Engineers.

Writes a single one-line fortune cookie message for a software
engineer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The fortune is a classic cookie opening ("You will ...") with the
twist coming from the engineer's own world: a trivial rename that
cascades into services the author never knew existed. The funniest
word sits at the very end.

The line is validated before it is written: exactly one line, no
more than 120 characters, non-blank, so the sealed gate (1 to 120
characters of UTF-8 text) always passes.
"""

import os
from pathlib import Path

FORTUNE = "You will rename a variable and break three services you did not know existed."

MAX_CHARS = 120


def validate_fortune(text: str) -> str:
    """Return the fortune unchanged, or raise if it breaks the gate."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("fortune must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"fortune is {len(stripped)} chars, over {MAX_CHARS}")
    return stripped


def fortune_length(text: str) -> int:
    """Character count of the fortune, as the gate counts it."""
    return len(validate_fortune(text))


def main() -> Path:
    # Note: the fortune uses only commas and periods, never an em dash,
    # so it reads exactly like a printed fortune cookie slip.
    fortune = validate_fortune(FORTUNE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(fortune + "\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    main()
