#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify script_03 scenarios: turn counts (20-25) and per-turn word counts. ASCII-only output."""
import re, sys

path = "script_03_link3.md"
start = int(sys.argv[1]) if len(sys.argv) > 1 else 1

bn = "০১২৩৪৫৬৭৮৯"
def bn2int(s):
    return int("".join(str(bn.index(c)) if c in bn else c for c in s))

with open(path, encoding="utf-8") as f:
    text = f.read()

parts = re.split(r"^## সিনারিও ", text, flags=re.M)[1:]
issues = 0
for p in parts:
    head = p.splitlines()[0]
    m = re.match(r"([০-৯0-9]+)", head)
    num = bn2int(m.group(1)) if m else 0
    if num < start:
        continue
    turns = re.findall(r"^\*\*([০-৯0-9]+)\.\s*(এজেন্টঃ|কাস্টমারঃ)\*\*\s*(.*)$", p, flags=re.M)
    tc = len(turns)
    flag_tc = "" if 20 <= tc <= 25 else "  <-- TURN COUNT OUT OF RANGE"
    print(f"S{num}: {tc} turns{flag_tc}")
    if flag_tc:
        issues += 1
    for tn, spk, txt in turns:
        wc = len(txt.split())
        is_expl = ("বিস্তারিত বুঝিয়ে বলছি" in txt)
        role = "AGT" if "এজেন্ট" in spk else "CUS"
        hi = 70 if is_expl else 60
        # flag: under 20, or over 30 (report the number so I can judge if it's a legit explanation)
        if wc < 20:
            print(f"    turn {tn} {role}: {wc} words  <-- TOO SHORT")
            issues += 1
        elif wc > 30:
            tag = "expl-ok" if (is_expl and wc <= hi) else ("long" if wc <= hi else "TOO LONG")
            print(f"    turn {tn} {role}: {wc} words  <-- {tag}")
            if tag == "TOO LONG":
                issues += 1
print(f"\nTOTAL HARD ISSUES: {issues}")
