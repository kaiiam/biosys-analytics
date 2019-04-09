#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-08
Purpose: Rock the Casbah
"""

import argparse
import sys
import Bio
import os
import re
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True,
        default='')

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')


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
    cdhit_file = args.cdhit
    protein_file = args.proteins
    outfile = args.outfile

    #print('boo')

    # if cdhit_file == '' or protein_file == '':
    #     die('usage: find_unclustered.py [-h] -c str -p str [-o str]\nfind_unclustered.py: error: the following arguments are required: -c/--cdhit, -p/--proteins')

    if not os.path.isfile(protein_file):
        print('--proteins "{}" is not a file'.format(protein_file), file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(cdhit_file):
        print('--cdhit "{}" is not a file'.format(cdhit_file), file=sys.stderr)
        sys.exit(1)


    id_re = re.compile('>gi'
                        '[|]'
                        '(?P<id_string>\d+)'   # capture year (group 1)
                        '[|]')

    clust_prots = []

    lines = 0

    with open(cdhit_file, 'r') as f:
        for line in f:
            # Do something with 'line'
            #print(line)
            #print(re.search('>gi|.*|', line))

            #lines += 1

            match = id_re.search(line)
            if match:
                clust_prots.append(match.group('id_string'))
            # else:
            #     print(line)
            # t = re.search(">gi|(\d{9})",line)
            # print(t)

    #print('lines: {}'.format(lines))

    #print(len(clust_prots))
    clust_prots = set(clust_prots)

    #print(len(clust_prots))

    out_fh = open(outfile, 'wt')

    num_skipped = 0
    num_taken = 0

    with open(protein_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            #print(record.id)

            record.id = re.sub('\|.*', '', record.id)
            #print(record.id)

            if record.id in clust_prots:
                #print(record.id)
                num_taken += 1
                SeqIO.write(record, out_fh, 'fasta')
            else:
                num_skipped += 1

    print('Wrote {} of {} unclustered proteins to "{}"'.format(num_taken,num_skipped,outfile))

# --------------------------------------------------
if __name__ == '__main__':
    main()
