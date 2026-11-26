#!/usr/bin/env python3
"""Two-Sentence Horror — prints the entry story to stdout.

The gate: exactly two sentences, 1 to 400 characters of UTF-8 text.
"""

STORY = (
    "I taught my daughter to knock twice when she needs me at night, "
    "and for a year she has knocked twice, every single night. "
    "Tonight the knock came twice, right on schedule, and when I opened "
    "the door, my daughter was fast asleep in her bed."
)


def get_line() -> str:
    # One story, assembled from its two sentences; the gate is checked
    # on the joined text so a future edit cannot silently break it.
    return STORY.strip()


def main() -> None:
    text = get_line()
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.count(".") == 2, "entry must be exactly two sentences"
    assert text.strip() == text and text, "entry must not be only whitespace"
    print(text)


if __name__ == "__main__":
    main()
