#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-02-19
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state_arg = args[0]


    ### Die if given a bad --state (too short, not made entirely of "-XO")
    # check 9 characters
    if len(state_arg) != 9:
        print('State "{}" must be 9 characters of only ., X, O'.format(state_arg))
        sys.exit(1)
    #check only . X or O
    for s in state_arg:
        if s not in ['.','X','O']:
            print('State "{}" must be 9 characters of only ., X, O'.format(state_arg))
            sys.exit(1)

    wins = [('X', 'XXX......'), ('O', 'OOO......'), ('X', '...XXX...'),
                ('O', '...OOO...'), ('X', '......XXX'), ('O', '......OOO'),
                ('X', 'X..X..X..'), ('O', 'O..O..O..'), ('X', '.X..X..X.'),
                ('O', '.O..O..O.'), ('X', '..X..X..X'), ('O', '..O..O..O'),
                ('X', 'X...X...X'), ('O', 'O...O...O'), ('X', '..X.X.X..'),
                ('O', '..O.O.O..')]


    for player, w_state in wins:
        ticks = 0
        for i, c in enumerate(w_state):
            #print(c, state_arg[i])
            if c == state_arg[i] and c == player:
                ticks += 1
                #print(ticks)
                if ticks == 3:
                    print('{} has won'.format(player))
                    return

    print('No winner')
# --------------------------------------------------
main()
