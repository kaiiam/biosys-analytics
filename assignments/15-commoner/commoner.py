#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-29
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging
import re
import io
from itertools import product
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input files', nargs=2, type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true',default=False)

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true',default=False)

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
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------
def uniq_words(file, min_len):
    #Read in input file, split into words filter for those >= min_len
    #use regex to remove characters which aren't numbers and letters and make lowercase
    words = [re.sub('[^a-zA-Z0-9]', '', x).lower() for x in file.read().split()]
    words = [w for w in words if len(w) >= min_len]
    return(set(words))


# --------------------------------------------------
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])

# --------------------------------------------------
def common(words1, words2, distance):
    prod = list(product(words1, words2))
    tup_list = []

    for w1, w2 in prod:
        if dist(w1, w2) <= distance:
            tup_list.append((w1, w2, dist(w1, w2)))

    return(sorted(tup_list))

# --------------------------------------------------
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1, file2 = args.positional
    min_len = args.min_len
    ham_dist = args.hamming_distance
    logfile = args.logfile
    table = args.table


    logging.basicConfig(
        filename=logfile,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
        )

    logging.debug('file1 = {}, file1 = {}'.format(file1,file2))

    if ham_dist < 0:
        die('--distance "{}" must be > 0'.format(ham_dist))


    words1 = uniq_words(file1, args.min_len)
    words2 = uniq_words(file2, args.min_len)
    common_words = common(words1, words2, args.hamming_distance)

    if len(common_words) == 0:
        print('No words in common.')
        sys.exit(0)


    header = ("word1", "word2", "distance")

    if not args.table:
        print("\t".join(header))
        for word in common_words:
            print("\t".join([str(i) for i in word]))

    else:
        print(tabulate(common_words, header, tablefmt="psql"))


# --------------------------------------------------
if __name__ == '__main__':
    main()
