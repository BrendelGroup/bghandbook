#!/usr/bin/env python
from __future__ import print_function
import argparse
import collections
import re
import sys

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('gff3', type=argparse.FileType('r'), help='GFF3 input')
    parser.add_argument('n', type=int, help='report aggregate length of N '
                        'adjacent iiLoci')
    return parser


def iilocus_length_from_gff3(infile, n=2):
    """
    Compute aggregate length of n consecutive iiLoci.

    In LocusPocus-produced GFF3, the length of each iiLocus is reported twice:
    in the `riil` attribute of the giLocus to the left, and the `liil` attribute
    of the giLocus to the right. This includes zero-length iiLoci (ziLoci),
    which are not otherwise explicitly reported in the GFF3 file.
    """
    iiloci = collections.deque()
    for line in infile:
        if '\tlocus\t' not in line or 'liil=' not in line:
            continue
        seqid = line.split('\t')[0]
        liilmatch = re.search('liil=(\d+)', line)
        assert liilmatch, line
        ilen = int(liilmatch.group(1))
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
