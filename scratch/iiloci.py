#!/usr/bin/env python
from __future__ import print_function
import argparse
import collections
import sys

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('gff3', type=argparse.FileType('r'), help='GFF3 input')
    parser.add_argument('n', type=int, help='report aggregate length of N '
                        'adjacent iiLoci')
    return parser


def iilocus_length_from_gff3(infile, n=2):
    iiloci = collections.deque()
    for line in infile:
        if '\tlocus\t' not in line or 'child_gene=' in line:
            continue
        fields = line.split('\t')
        seqid = fields[0]
        ilen = int(fields[4]) - int(fields[3]) + 1
        if len(iiloci) > 0 and iiloci[0][0] != seqid:
            iiloci = collections.deque()
        iiloci.append((seqid, ilen))
        if len(iiloci) == n:
            aggregate_length = sum([iilocus[1] for iilocus in iiloci])
            yield seqid, aggregate_length
            iiloci.popleft()


def main(args):
    for seqid, length in iilocus_length_from_gff3(args.gff3, args.n):
        print(seqid, length, sep='\t')


if __name__ == '__main__':
    main(get_parser().parse_args())
