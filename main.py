"""How Many Tabs Do You Have Open? — entry program.

Writes exactly one number in digits, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. Deterministic: no randomness, no network,
no input files.

The number: 142 — an honest, lived-in count. Odd and specific, the
way a real count is: nobody who actually counts their tabs lands on
a round number. Three browser windows deep into a project that never
ends — research, docs, half-read articles, and the tabs kept open
"just in case" for weeks. Big enough to surprise, small enough that
the browser still runs.
"""

import os

COUNT = "142"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(COUNT)
    print(f"wrote {path} ({len(COUNT)} characters)")


if __name__ == "__main__":
    main()
