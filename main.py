"""Two-Sentence Horror — a make.fun bounty entry.

Writes the story to the path in ENTRY_OUTPUT (default /output/entry.txt).
Pure standard library, deterministic, no network.
"""

import os

SENTENCE_ONE = (
    "Every night since the funeral, I read my daughter a bedtime story "
    "through the nursery monitor, because the grief counselor said a "
    "ritual would help me let go."
)

SENTENCE_TWO = (
    "Last night I stopped mid-sentence, and a small voice \u2014 hers, "
    "word-perfect \u2014 finished it from inside her empty room."
)

STORY = SENTENCE_ONE + " " + SENTENCE_TWO


def main():
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(output, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
