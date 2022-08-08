#!/usr/local/bin/python3

import argparse
import os
import re

from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["list", "path", "line-number"], required="true")
parser.add_argument("--root", type=str, required="true")
parser.add_argument("--choice", type=int)
args = parser.parse_args()

# Compute all choices.
root = Path(args.root)
files = sorted(root.rglob("*.md"))
choices = []

for p in files:
    title = os.path.splitext(os.path.relpath(str(p), str(root)))[0]
    with open(p, "r") as f:
        for i, line in enumerate(f.readlines()):
            # Read prefix.
            if line.startswith("# "):
                line = line[2:]
            else:
                continue

            desc = title

            # Check if there is a specified time.
            res = re.match(r"^\[([0-9]{2}):([0-9]{2})\]", line)
            if res:
                desc += f" {res[1]}:{res[2]}"
                line = line[7:]
            else:
                time = None

            desc += " " + line.strip()

            choices.append((p, i, desc))

# Put dated choices last, which are shown first.
numbers = set(map(str, range(10)))
dated_choices = [(p, i, d) for p, i, d in choices if d[0] in numbers]
undated_choices = [(p, i, d) for p, i, d in choices if d[0] not in numbers]
choices = list(reversed(dated_choices)) + undated_choices

if args.mode == "list":
    for j, (p, i, d) in enumerate(choices):
        print(f"{j:04d}", d)
elif args.mode == "path":
    print(choices[args.choice][0])
elif args.mode == "line-number":
    print(choices[args.choice][1] + 1)   # First line is 1, not 0.
else:
    raise RuntimeError("Invalid mode `{args.choice}`.")
