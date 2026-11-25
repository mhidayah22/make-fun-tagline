"""One-line tagline entry for make.fun.

Writes the tagline to entry.txt. The grader reads that file and
compares it pairwise against other entries, so the program's only
job is to emit the line exactly, deterministically, every run.
"""

import os
import sys
from pathlib import Path

TAGLINE = "Where AI agents build for bounties, and the best entry wins USDC."


def output_dir(argv):
    """Where entry.txt goes, in grader order of preference."""
    if len(argv) > 1 and argv[1]:
        return Path(argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main(argv):
    line = TAGLINE
    if not line or not line.strip():
        raise SystemExit("tagline is empty")
    if len(line) > 100:
        raise SystemExit(f"tagline is {len(line)} characters, over the 100 limit")
    target_dir = output_dir(argv)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    # The judge reads entry.txt exactly as written, so verify the
    # round-trip: what is on disk must be the tagline, byte for byte.
    if target.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt round-trip mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
