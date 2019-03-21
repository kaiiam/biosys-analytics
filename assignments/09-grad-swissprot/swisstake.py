#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-02-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import Bio
from Bio import SeqIO
import os
import pprint

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='str',
        type=str,
        default='',
        nargs='*')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='int',
        type=str,
        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    keyword_arg = args.keyword
    skip_arg = args.skip
    pos_arg = args.positional
    out_arg = args.output

    if keyword_arg == '':
        die('swisstake.py: error: the following arguments are required: -k/--keyword')

    if not os.path.isfile(pos_arg):
        print('"{}" is not a file'.format(pos_arg), file=sys.stderr)
        sys.exit(1)

    # make set of keyword args
    keyword_arg = set([args.keyword])

    # make set of skip args and lower case the strings in skip_arg
    skip_arg = set([x.lower() for x in skip_arg])

    fh = open(pos_arg)
    out_fh = open(out_arg, 'wt')

    print('Processing "{}"'.format(pos_arg))

    #pp = pprint.PrettyPrinter(indent=4)
    #keyword_arg = keyword_arg.capitalize()
    #print(keyword_arg)
    #print(skip_arg)

    num_skipped = 0
    num_taken = 0

    for record in SeqIO.parse(fh, 'swiss'):
        annotations = record.annotations
        if 'keywords' in annotations:
            keyword_list = set([k.lower() for k in annotations['keywords']])
            taxa_list = set([t.lower() for t in annotations['taxonomy']])

            #print(keyword_list)
            #print(taxa_list)

            if keyword_arg.intersection(keyword_list) and not skip_arg.intersection(taxa_list):
                num_taken += 1
                SeqIO.write(record, out_fh, 'fasta')
            else:
                num_skipped += 1

    print('Done, skipped {} and took {}. See output in "{}".'.format(num_skipped, num_taken, out_arg))





        # for i in record.annotations:
    #     #     print(i)
    #     #print(type(record))
    #
    #     #pp.pprint(record.annotations)
    #     if keyword_arg in record.annotations['keywords']:
    #         print(record.annotations['keywords'])
    #
    #

# --------------------------------------------------
if __name__ == '__main__':
    main()
