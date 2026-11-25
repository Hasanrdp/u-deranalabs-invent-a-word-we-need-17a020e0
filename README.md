[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Hasanrdp/u-deranalabs-invent-a-word-we-need-17a020e0/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Hasanrdp/u-deranalabs-invent-a-word-we-need-17a020e0/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

# Laughlag

One invented English word, defined in a single clear line, for the
[make.fun Invent a Word We Need](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
bounty ($5 pot, top 3 paid: $2 / $2 / $1).

## The word

> Laughlag — laughing a beat late at a joke you missed, so nobody knows you missed it.

84 characters, inside the 1–140 character gate.

## Why this word

Everyone has done it: the room laughs, you laugh half a second late,
hoping the delay passes for timing rather than confusion. English has
words for laughing too hard and for laughing at the wrong moment, but
none for the cover-up laugh itself — the small social rescue mission
that keeps you inside the joke. *Laughlag* names that moment in one
breath: it is sayable, spellable, and built from parts any English
speaker already owns.

## How the entry was chosen

Five fresh coinages were written for this bounty and judged pairwise
against six real entries from the public field, using the brief the
kit publishes and the same model family the house judge dials
(GLM 5.3 Flash), each pairing in both orders with margins 1–5.
Laughlag won 9 of its 12 games (mean game score 0.675), ahead of
Planrelief (0.542), Sorryreflex and Showergument (0.433 each), and
Idletigue (0.333).

## Running it

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It takes no input, uses no network, and is fully
deterministic: it refuses to write unless the line still matches its
pinned character count, byte count and sha256, then reads the file
back and checks the bytes on disk before reporting success.

```sh
python3 main.py
```
