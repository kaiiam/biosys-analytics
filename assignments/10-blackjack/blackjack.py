#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-03-27
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
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='A boolean flag for player hiting', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='A boolean flag for dealer hiting', action='store_true')


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
    seed = args.seed
    player_hits = args.player_hits
    dealer_hits = args.dealer_hits

    random.seed(seed)
    #random.Random(seed_arg)

    suites = list('♥♠♣♦')

    # numbs = list(range(2,11))
    # face_cards = list('JQKA')
    #
    # numbs_cards = [str(s) for s in numbs]
    # numbs_cards += face_cards

    #create cards and values
    cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #create dict of card values
    values = dict(zip(cards,values))

    #produce the deck of chards
    deck = list(product(suites, cards))

    #sort the deck of cards
    deck.sort()

    #shuffle deck of cards
    random.shuffle(deck)
    #print(deck)

    dealer = []
    player = []

    cards_dealt = 4

    while cards_dealt:
        player.append(deck.pop())
        cards_dealt -= 1

        dealer.append(deck.pop())
        cards_dealt -= 1

    if player_hits is True:
        player.append(deck.pop())

    if dealer_hits is True:
        dealer.append(deck.pop())

    player_sum = sum([values[t[1]] for t in player])

    dealer_sum = sum([values[t[1]] for t in dealer])

    dealer_string = ' '.join([''.join(x) for x in dealer])

    player_string = ' '.join([''.join(x) for x in player])

    #print out results:
    print('D [{:>2}]: {}'.format(dealer_sum, dealer_string ))
    print('P [{:>2}]: {}'.format(player_sum, player_string ))

    #Check if the player has more than 21; if so, print 'Player busts! You lose, loser!' and exit(0)
    if player_sum > 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)

    #Check if the dealer has more than 21; if so, print 'Dealer busts.' and exit(0)
    if dealer_sum > 21:
        print('Dealer busts.')
        sys.exit(0)

    #Check if the player has exactly 21; if so, print 'Player wins. You probably cheated.' and exit(0)
    if player_sum == 21:
        print('Player wins. You probably cheated.')
        sys.exit(0)

    #Check if the dealer has exactly 21; if so, print 'Dealer wins!' and exit(0)
    if dealer_sum == 21:
        print('Dealer wins!')
        sys.exit(0)

    #check if dealer and player should hiting
    if dealer_sum < 18:
        print('Dealer should hit.')
    if player_sum < 18:
        print('Player should hit.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
