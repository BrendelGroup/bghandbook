#!/usr/bin/env python
# Usage: python feature_count.py < input.gff3

from __future__ import print_function
import sys

counts = dict()
for line in sys.stdin:
    values = line.split('\t')
    if len(values) != 9:
        continue
    feature_type = values[2]
    if feature_type not in counts:
        counts[feature_type] = 0
    counts[feature_type] += 1

for feature_type in counts:
    print(feature_type, counts[feature_type], sep='\t')
