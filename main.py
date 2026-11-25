#!/usr/bin/env python3
"""The Funniest Office Joke — writes one single-line office joke to /output/entry.txt.

The joke: a manager calls a meeting about too many meetings, then books a
follow-up about the first meeting. Concrete, universally recognised office
detail (the meeting about meetings, action items); the turn lands in the
last words — the cure for too many meetings is another meeting. 142 chars,
inside the 1-200 gate.
"""
import os

JOKE = (
    "My manager called a meeting to find out why we have too many meetings, "
    "then booked a follow-up to discuss the action items from the first one."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
