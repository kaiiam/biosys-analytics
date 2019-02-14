#!/usr/bin/env python3
"""
Author : Kai Blumberg
Date   : 2019-02-12
Purpose: Rock the Casbah (or similar)
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str)

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int)

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
    state_arg = args.state
    player_arg = args.player
    cell_arg = args.cell

    ### Die if given a bad --state (too short, not made entirely of "-XO")
    # check 9 characters
    if len(state_arg) != 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state_arg))
        sys.exit(1)
    #check only . X or O
    for s in state_arg:
        if s not in ['.','X','O']:
            print('State "{}" must be 9 characters of only ., X, O'.format(state_arg))
            sys.exit(1)

    #Die on invalid player:
    if not player_arg:
        pass
    elif player_arg not in ['X','O']:
        print('Invalid player "{}", must be X or O'.format(player_arg))
        sys.exit(1)

    #Die on invalid cell:
    if cell_arg is None:
        pass
    elif not 0 < cell_arg <= 9:
        print('Invalid cell "{}", must be 1-9'.format(cell_arg))
        sys.exit(1)

    #Handle the instance where you got one of --player or --cell but not both
    if cell_arg is None and player_arg in ['X','O']:
        print('Must provide both --player and --cell')
        sys.exit(1)

    if player_arg is None and cell_arg is not None:
        print('Must provide both --player and --cell')
        sys.exit(1)


    #split the state string into a list so it can be altered
    state_list = list(state_arg)
    #print(state_list)

    #when the state for a cell is ".", print the number of the cell
    for count, s in enumerate(state_list):
        if s == '.':
            state_list[count] = str(count+1)


    #Mutate an initial state as described by --cell and --player
    if cell_arg is None:
        pass
    elif not player_arg:
        pass
    elif state_list[cell_arg-1] in ['X','O']:
        print('Cell {} already taken'.format(cell_arg))
        sys.exit(1)


    if cell_arg is None:
        pass
    elif not player_arg:
        pass
    else:
        state_list[cell_arg-1] = player_arg


    #join the state list back together into a string to print
    #https://stackoverflow.com/questions/1228299/change-one-character-in-a-string
    print_string = ''.join(state_list)
    #print(print_string)








    ### Print the Board
    #making use of the reassembled print_string
    # Divider string
    divider = '-------------'
    print(divider)

    for count, s in enumerate(print_string):
        print('| {} '.format(print_string[count]), end='')
        if (count+1)%3 == 0:
            print('|', end='')
            print('')
            print(divider)

    # print('str_arg = "{}"'.format(str_arg))
    # print('int_arg = "{}"'.format(int_arg))
    # print('flag_arg = "{}"'.format(flag_arg))
    # print('positional = "{}"'.format(pos_arg))

# --------------------------------------------------
if __name__ == '__main__':
    main()
