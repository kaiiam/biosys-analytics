#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-02-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import shutil
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FASTA', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='A named string argument',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--int',
        help='Dividing line for percent GC',
        metavar='pct_gc',
        type=int,
        default=50)

    # parser.add_argument(
    #     '-f', '--flag', help='A boolean flag', action='store_true')

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
    outdir_arg = args.outdir
    pct_gc_arg = args.int
    pos_arg = args.positional

    num_seq = 0

    if not 1 <= pct_gc_arg <= 100:
        print('--pct_gc "{}" must be between 0 and 100'.format(pct_gc_arg))
        sys.exit(1)

    #create outdir
    if os.path.exists(outdir_arg):
        shutil.rmtree(outdir_arg)
    os.makedirs(outdir_arg)

    for file in pos_arg:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file), file=sys.stderr)

    for file in pos_arg:

        #check if positional arguments are files
        if os.path.isfile(file):
            basename = os.path.basename(file)
            #print(basename)

            #make low_gc outstring file path
            names = os.path.splitext(basename)
            low_str = names[0] + '_low' + names[1]
            low_file_path = os.path.join(outdir_arg, low_str)
            low_fh = open(low_file_path, 'wt')

            #make high_gc outstring file path
            high_str = names[0] + '_high' + names[1]
            high_file_path = os.path.join(outdir_arg, high_str)
            high_fh = open(high_file_path, 'wt')

            #print(file)
            with open(file) as f:
                for rec in SeqIO.parse(f, "fasta"):
                    num_seq += 1

                    gc_count=0
                    for i, c in enumerate(rec):
                        if c == 'G' or c == 'C':
                            gc_count +=1
                    # calculate GC content:
                    gc_content = int((gc_count / (i+1))*100)
                    #print(gc_content)

                    if gc_content >= pct_gc_arg:
                        SeqIO.write(rec, high_fh, "fasta")
                    else:
                        SeqIO.write(rec, low_fh, "fasta")


    print('Done, wrote {} sequences to out dir "{}"'.format(num_seq, outdir_arg))

# --------------------------------------------------
if __name__ == '__main__':
    main()
