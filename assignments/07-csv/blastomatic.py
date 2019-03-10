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
    centroid_list = []
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            centroid = [row['centroid'], row['genus'], row['species'] ]
            centroid_list.append(centroid)
            #print(centroid)

    #print(centroid_list)

    #read and open the inputfile:
    out_list = [['seq_id', 'pident', 'genus', 'species']]
    with open(in_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            record = list(row.items())
            #print(record[1][1])
            for i, cl in enumerate(centroid_list):

                if record[1][1] == centroid_list[i][0]:
                    #print('its in')
                    #pass
                    joint_rec = [record[1][1], record[2][1], centroid_list[i][1], centroid_list[i][2]]
                    out_list.append(joint_rec)

            else:
                print('Cannot find seq "{}" in lookup'.format(record[1][1]), file=sys.stderr)



    # for a, b, c, d in out_list:
    #     print(a,b,c,d)

    if out_file != '':
        #print('we have an out')
        with open(str(out_file), 'w') as outf:
            writer = csv.writer(outf, delimiter='\t')
            writer.writerows(out_list)

            #
            # for record in SeqIO.parse("/home/fil/Desktop/420_2_03_074.fastq", "fastq"):
            #     writer.writerow([record.id, record.seq, record.format("qual")])


    else:
        # for a, b, c, d in out_list:
        #     print(a,b,c,d)
        #for x in out_list:
        for a, b, c, d in out_list:
            print('{}   {}  {}  {}'.format(a, b, c, d))

# --------------------------------------------------
if __name__ == '__main__':
    main()
