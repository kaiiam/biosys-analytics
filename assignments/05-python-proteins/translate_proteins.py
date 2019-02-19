#!/usr/bin/env python3
"""
Author : Kai Blumberg
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os #to check if codon input is of type file

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--out',
        help='Output filename',
        metavar='str',
        type=str,
        default='out.txt')

    # parser.add_argument(
    #     '-f', '--flag', help='A boolean flag', action='store_true')

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
    codons_arg = args.codons
    out_arg = args.out
    #flag_arg = args.flag

    #Die on a bad --codons argument:
    if not os.path.isfile(codons_arg):
        print('--codons "{}" is not a file'.format(codons_arg))
        sys.exit(1)

    #read the codons in as a dictionary
    codons_dict = {}
    with open(codons_arg, 'r') as in_file:
        for line in in_file:
            line_array = line.split()
            codon_DNA = line_array[0].upper()
            codon_PRO = line_array[1]
            codons_dict[codon_DNA] = codon_PRO

    #Extract Codons from DNA
    string = pos_arg.upper()
    k = 3
    n = len(string) - k + 1

    out_string_list = []

    for i in range(0, n, k):
        if string[i:i+k] in codons_dict:
            #print('ohYA')
            #print(codons_dict[string[i:i+k]])
            out_string_list.append(codons_dict[string[i:i+k]])
        else:
            #print('SHIT')
            out_string_list.append('-')
        #print(string[i:i+k])

    #print(out_string_list)

    with open(out_arg,'w') as f:
        f.write(''.join(out_string_list))

    print('Output written to "{}"'.format((str(out_arg))))

    #print('pos_arg = "{}"'.format(pos_arg))
    #print('codons_arg = "{}"'.format(codons_arg))
    #print('out_arg = "{}"'.format(out_arg))
    #print('flag_arg = "{}"'.format(flag_arg))



# --------------------------------------------------
if __name__ == '__main__':
    main()

