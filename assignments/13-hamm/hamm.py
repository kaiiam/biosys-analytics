#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-15
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='File inputs', nargs=2)


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

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
def dist(s1, s2):
    """Haming distance calculation function"""

    dist = abs(len(s1) - len(s2))
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            dist +=1
    logging.debug('s1 = {} s2 = {} d = {}'.format(s1, s2, dist))
    return(dist)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    debug_arg = args.debug
    f1, f2 = args.files

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
        )

    logging.debug('file1 = {}, file1 = {}'.format(f1,f2))

    for x in args.files:
        if not os.path.isfile(x):
            print('"{}" is not a file'.format(x), file=sys.stderr)
            sys.exit(1)


    words1 = open(f1).read().split()

    words2 = open(f2).read().split()

    dist_count = 0

    for w1, w2 in zip(words1, words2):
        dist_count += dist(w1, w2)

    print(dist_count)


# --------------------------------------------------
if __name__ == '__main__':
    main()
