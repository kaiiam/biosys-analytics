#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-03-25
Purpose: Rock the Casbah
"""

import argparse
import sys
from itertools import product
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

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

def tuple_to_str(tup):
    #out = ''.join(reversed(tup))
    out = ''.join(tup)
    return(out)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed_arg = args.seed

    random.seed(seed_arg)
    #random.Random(seed_arg)

    #suites = list('♠♣♦♥')
    suites = list('♥♠♣♦')
    #suites = list('♣♦♥♠')

    numbs = list(range(2,11))
    face_cards = list('JQKA')

    numbs_cards = [str(s) for s in numbs]
    numbs_cards += face_cards

    #numbs_cards = ['2','3','4','5','6','7','8','9','10','J','Q', 'K', 'A']

    #deck = list(product(numbs_cards, suites))
    deck = list(product(suites, numbs_cards))

    deck.sort()

    #print(deck)

    ##assign values to the decks cards in a dict
    values = {}
    for i, x in enumerate(numbs_cards):
        values.update({x: i})
        #print(i,x)

    #print(values['2'])

    random.shuffle(deck)
    #print(deck)

    player_1 = ()
    player_2 = ()

    p1_count = 0
    p2_count = 0

    while len(deck) > 0:
        player_1 = deck.pop()
        player_2 = deck.pop()

        # p1 = values[player_1[0]]
        # p2 = values[player_2[0]]
        p1 = values[player_1[1]]
        p2 = values[player_2[1]]

        if p1 > p2:
            outcome = 'P1'
            p1_count += 1
        if p2 > p1:
            outcome = 'P2'
            p2_count += 1
        if p1 == p2:
            outcome = 'WAR!'

        #print('{} {} {}'.format(tuple_to_str(player_1), tuple_to_str(player_2), outcome))

        if len(''.join(player_1)) > 2:
            p1_out = ''.join(player_1)
        else:
            p1_out = ' ' + ''.join(player_1)

        if len(''.join(player_2)) > 2:
            p2_out = ''.join(player_2)
        else:
            p2_out = ' ' + ''.join(player_2)

        print('{} {} {}'.format(p1_out,p2_out,outcome))

        #print(p2_out)

        # if len(''.join(player_2)) > 2:
        #     print('{} {} {}'.format(''.join(player_1), ''.join(player_2), outcome))
        #
        #     if len(''.join(player_1)) > 2:
        #         print('{} {} {}'.format(''.join(player_1), ''.join(player_2), outcome))
        #
        # else:
        #     print('{}  {} {}'.format(''.join(player_1), ''.join(player_2), outcome))

    if p1_count > p2_count:
        winner = 'Player 1 wins'
    if p1_count < p2_count:
        winner = 'Player 2 wins'
    if p1_count == p2_count:
        winner = 'DRAW'

    print('P1 {} P2 {}: {}'.format(p1_count, p2_count, winner))

    # player_1 = deck.pop()
    # print(player_1)
    #
    # out = ''.join(reversed(player_1))
    # print(out)



# --------------------------------------------------
if __name__ == '__main__':
    main()
