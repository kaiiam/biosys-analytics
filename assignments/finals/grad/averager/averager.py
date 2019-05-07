#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from os.path import basename

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Average all the numbers in a document',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input file(s)',nargs='+')

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
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pos_arg = args.positional

    # for x in pos_arg:
    #     if not os.path.isfile(x):
    #         print('"{}" is not a file'.format(x), file=sys.stderr)
    #         sys.exit(0)

    for file in pos_arg:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file), file=sys.stderr)
            sys.exit(0)


        with open(file, 'r') as f:
            words = f.read().split()
            words = [x.lower() for x in words]
            #print(words)

            id_re = re.compile('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')

            c_words = []
            for w in words:
                match = id_re.search(w)
                if match:
                    c_words.append(w)

            c_words = [re.sub('[^0-9\-.]', '', x).lower() for x in c_words]

            numbs = []
            sum = 0
            for w in c_words:
                # for c in w:
                #     if c[-1] == '.':
                #         print('yes')
                if w[-1] == '.':
                    #print(w)
                    w = w[:-1]
                    #print(w)


                numbs.append(float(w))
                sum += float(w)
                #print(w)

            length = len(numbs)
            if length == 0:
                #zero = '0.00'
                print('{:10.02f}: {}'.format(0.00, basename(file)))

            else:
                avg = sum / length
                print('{:10.02f}: {}'.format(avg, basename(file)))

            # print(numbs)
            # print(sum)
            # print(length)
            #
            #
            # print(basename(file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
