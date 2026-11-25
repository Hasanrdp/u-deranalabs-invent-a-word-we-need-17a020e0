#!/usr/bin/env python3
"""Entry for make.fun u-deranalabs-invent-a-word-we-need-17a020e0.

One invented English word, defined in a single clear line, written to
/output/entry.txt. The line is 84 characters, inside the gate's 1-140.

The program takes no input, touches no network and never rolls a die:
every run writes the same 86 bytes. Before it writes anything it checks
the line against its pinned length and sha256, and after writing it reads
the file back and checks the bytes on disk, so a drifted line fails here
with a loud error instead of quietly failing the grader's gate.
"""

import hashlib
import os
import sys

WORD = (
    "Laughlag \u2014 laughing a beat late at a joke you missed, "
    "so nobody knows you missed it."
)

# Pinned so the program can prove it wrote the line that was pre-judged.
EXPECTED_CHARS = 84
EXPECTED_BYTES = 86
EXPECTED_SHA256 = "bd8ea424128aa24ab7a4a4c4cf91a2ca678618dc8c94205dc5966bfd9d959eed"

OUTPUT_PATH = "/output/entry.txt"


def verify(text: str) -> bytes:
    """Return the line's bytes, or exit if they drifted from the pin."""
    encoded = text.encode("utf-8")
    if len(text) != EXPECTED_CHARS:
        sys.exit(f"entry is {len(text)} characters, expected {EXPECTED_CHARS}")
    if len(encoded) != EXPECTED_BYTES:
        sys.exit(f"entry is {len(encoded)} bytes, expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit(f"entry sha256 {digest} does not match pinned {EXPECTED_SHA256}")
    if text != text.strip():
        sys.exit("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    return encoded


def main() -> None:
    payload = verify(WORD)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)
    with open(OUTPUT_PATH, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        sys.exit("read-back mismatch: bytes on disk differ from the pinned line")
    if hashlib.sha256(on_disk).hexdigest() != EXPECTED_SHA256:
        sys.exit("read-back mismatch: sha256 on disk differs from the pinned hash")
    print(f"wrote {len(on_disk)} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
