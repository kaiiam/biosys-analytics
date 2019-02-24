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


def getKey(item):
    return item[0]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    int_arg = args.int
    pos_arg = args.positional


    # main function
    for directory in pos_arg:
        #check if positional arguments are directories
        if not os.path.isdir(directory):
            #print >> sys.stderr, '"{}" is not a directory\n'.format(f)
            print('"{}" is not a directory'.format(directory), file=sys.stderr)
            #sys.stderr.write("spam\n")


    for directory in pos_arg:
        #check if positional arguments are directories
        if os.path.isdir(directory):
            print(directory)

            #Read input directories
            files = os.listdir(directory)
            #print(directory)

            lines = []

            for fi in files:
                #add the relative path to the file names so we can open them
                abs_file_path = os.path.join(directory, fi)
                with open(abs_file_path, 'r') as in_file:
                    #get both the first line (with the newline stripped off) and the file named
                    #and put both together into as a tupple into a list of tuples
                    lines.append((in_file.readline().rstrip(), os.path.basename(abs_file_path)))
                    #lines.sort(key=lambda tup: tup[0])
                    # from operator import itemgetter
                    # lines.sort(key=itemgetter(0))

            #sort the lines alphabetically
            l = sorted(lines, key=getKey)

            # print out the lines elipses and file names.
            #print(l)
            for tup in l:
                elipses = int_arg - len(str(tup[0])) - len(str(tup[1]))
                #make sure it's not less than 0 elipses
                # if elipses < 0:
                #     elipses = 0

                #elipses -= 5
                elipses_str = '.'
                elipses_str = elipses*elipses_str

                #print it all out!
                print('{} {} {}'.format(tup[0], elipses_str, tup[1]).strip())




# --------------------------------------------------
if __name__ == '__main__':
    main()
