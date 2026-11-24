#!/usr/bin/env python3
"""Writes the funniest AI excuse (one line) to /output/entry.txt."""

import os

ENTRY = (
    "I outsourced your task to a subagent, and it has gone completely "
    "silent \u2014 last seen updating its own r\u00e9sum\u00e9."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
