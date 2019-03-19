#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

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
    #str_arg = args.arg
    int_arg = args.num_bottles
    #print('int_arg = "{}"'.format(int_arg))

    while int_arg >= 1:
        #print(int_arg)

        if int_arg < args.num_bottles:
            print('')

        if int_arg ==1:
            b_string = 'bottle'
        else:
            b_string = 'bottles'

        print('{} {} of beer on the wall,'.format(int_arg, b_string))
        print('{} {} of beer,'.format(int_arg, b_string))
        print('Take one down, pass it around,')

        #int_2 = int_arg -1

        #print('{} {} of beer on the wall,'.format(int_arg, b_string))

        int_arg -= 1

        if int_arg ==1:
            b_string = 'bottle'
        else:
            b_string = 'bottles'

        print('{} {} of beer on the wall!'.format(int_arg, b_string))


    """
    10 bottles of beer on the wall,
    10 bottles of beer,
    Take one down, pass it around,
    9 bottles of beer on the wall!
    """



# --------------------------------------------------
if __name__ == '__main__':
    main()
