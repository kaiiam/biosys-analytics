#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-24
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
from collections import defaultdict

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='File input(s)',nargs='+', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
    sort_arg = args.sort
    min_arg = args.min
    pos_arg = args.positional


    for file in pos_arg:
        #print(file)
        ## open file as TextIOwrapper and parse into list of words
        words = file.read().split()

        #use regex to remove characters which aren't numbers and letters and make lowercase
        words = [re.sub('[^a-zA-Z0-9]', '', x).lower() for x in words]

        #print(words)

        words.remove('')

        word_counts = defaultdict(int)

        for w in words:
            word_counts[w] +=1
        #print(word_counts)


        # #set a min number of words
        # for item in word_counts.items():
        #     if item[1] <= min_arg:
        #         #print(item[0], item[1])
        #         word_counts.pop(item[0], item[1])


        if sort_arg == 'word':
            pairs = sorted([(word, count) for word, count in word_counts.items()])
            for word, count in pairs:
                if count >= min_arg:
                    print('{:20} {}'.format(word, count))
        elif sort_arg == 'frequency':
            pairs = sorted([(count, word) for word, count in word_counts.items()])
            for count, word in pairs:
                if count >= min_arg:
                    print('{:20} {}'.format(word, count))


# --------------------------------------------------
if __name__ == '__main__':
    main()
