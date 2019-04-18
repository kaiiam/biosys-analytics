#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-17
Purpose: Rock the Casbah
"""

import argparse
import sys
import Bio
import os
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='A positional argument')


    parser.add_argument(
        '-k',
        '--int',
        help='K size of overlap',
        metavar='int',
        type=int,
        default=3)

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
def find_first_kmer(in_string, k):
    """function to find the first k mer of given length from string"""
    r_string = str(in_string[0:k])
    return(r_string)

# --------------------------------------------------
def find_kmers(in_string, k):
    """function to find k mers of given length from string"""
    n = len(in_string) - k + 1
    kmers_list = []
    for i in range(0, n):
        kmers_list.append(in_string[i:i+k])
    return(kmers_list)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    int_arg = args.int
    pos_arg = args.positional


    if int_arg <= 0: # or not int_arg.isdigit()
        print('-k "{}" must be a positive integer'.format(int_arg))
        sys.exit(1)

    if not os.path.isfile(pos_arg):
        print('"{}" is not a file'.format(pos_arg), file=sys.stderr)
        sys.exit(1)

    kmer_start = {}
    kmer_end = {}

    with open(pos_arg, 'r') as f:
        for record in SeqIO.parse(f, "fasta"):
            #start = find_kmers(record.seq, int_arg)
            #kmer_start[record.id]=(find_first_kmer(record.seq, int_arg))
            #kmer_end[record.id]=(find_first_kmer(record.seq[::-1], int_arg))

            kmer_start[record.id]=(find_kmers(record.seq, int_arg)[0])
            kmer_end[record.id]=(find_kmers(record.seq, int_arg)[-1])



    # for x,y in kmer_start.items():
    #     print(x,y)
    #
    # print('end:')
    #
    # for x,y in kmer_end.items():
    #     print(x,y)



    for e_key, e_value in kmer_end.items():
        for s_key, s_value in kmer_start.items():
            if e_value in s_value:
                if e_key is not s_key:
                    #print(e_key, e_value, s_key, s_value)
                    print(e_key, s_key)



    #print(find_kmers('ACTGCA', 3))
# --------------------------------------------------
if __name__ == '__main__':
    main()
