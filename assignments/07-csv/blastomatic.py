#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-03-09
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import csv
import collections
import pandas as pd


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    anno_file = args.annotations
    out_file = args.outfile
    in_file = args.positional

    if not os.path.isfile(in_file):
        print('"{}" is not a file'.format(in_file), file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(anno_file):
        print('"{}" is not a file'.format(anno_file), file=sys.stderr)
        sys.exit(1)


    #read and open the annotations file
    centroid_dict = {}
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            #centroid_dict.update({row['centroid']: {'genus': row['genus'], 'species': row['species']}})
            centroid_dict[row['centroid']] = row


    out_list = ['seq_id', 'pident', 'genus', 'species']

    #setup where we'll print the file handel standardout or to the input_arg out_file
    if out_file != '':
        f = open(out_file, 'a')
    else:
        f = sys.stdout

    print('\t'.join(out_list), file=f)

    #open the inputfile, find the corresponding annotation records and print the relevant data
    with open(in_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=('qaccver', 'saccver', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send' 'evalue' 'bitscore'))
        for row in reader:
            id = row['saccver']
            pident = row['pident']
            if id in centroid_dict:
                if centroid_dict[id]['genus'] == '':
                    genus = 'NA'
                else:
                    genus = centroid_dict[id]['genus']

                if centroid_dict[id]['species'] == '':
                    species = 'NA'
                else:
                    species = centroid_dict[id]['species']

                out_line = [id, pident, genus, species]


                #out_line = [row['saccver'], row['pident'],centroid_dict[id]['genus'], centroid_dict[id]['species']]

                print('\t'.join(out_line), file=f)

            else:
                print('Cannot find seq "{}" in lookup'.format(id), file=sys.stderr)

# --------------------------------------------------
if __name__ == '__main__':
    main()
