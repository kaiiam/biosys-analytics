#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-02-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='A positional argument', nargs='+')

    parser.add_argument(
        '-w',
        '--int',
        #help='A named integer argument',
        metavar='int',
        type=int,
        default=50)

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
    int_arg = args.int
    pos_arg = args.positional

    #check if positional arguments are directories
    for f in pos_arg:
        if not os.path.isdir(f):
            #print >> sys.stderr, '"{}" is not a directory\n'.format(f)
            print('"{}" is not a directory'.format(f), file=sys.stderr)
            sys.exit(1)

    #sys.stderr.write("spam\n")


    print('int_arg = "{}"'.format(int_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
