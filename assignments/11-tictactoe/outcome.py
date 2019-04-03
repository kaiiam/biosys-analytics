#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-03
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STATE', help='A positional argument')


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

    pos_arg = args.positional


    passing_re = re.compile('[XO.]{9}')


    if not passing_re.match(pos_arg):
        print('State "{}" must be 9 characters of only ., X, O'.format(pos_arg))
        sys.exit(0)


    wins = [('X', 'XXX......'), ('O', 'OOO......'), ('X', '...XXX...'),
                ('O', '...OOO...'), ('X', '......XXX'), ('O', '......OOO'),
                ('X', 'X..X..X..'), ('O', 'O..O..O..'), ('X', '.X..X..X.'),
                ('O', '.O..O..O.'), ('X', '..X..X..X'), ('O', '..O..O..O'),
                ('X', 'X...X...X'), ('O', 'O...O...O'), ('X', '..X.X.X..'),
                ('O', '..O.O.O..')]

    for winner, state in wins:
        #print(winner, state)
        #print(winner, re.match(state, pos_arg))
        if re.match(state, pos_arg):
            #print(winner,state, pos_arg )
            print('{} has won'.format(winner))
            sys.exit(0)


    print('No winner')


# --------------------------------------------------
if __name__ == '__main__':
    main()
