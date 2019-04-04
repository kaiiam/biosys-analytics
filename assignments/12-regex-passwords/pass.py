#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-03
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    pass_arg = args[0]
    alt_arg = args[1]

    compile_str1 = pass_arg

    compile_str2 = pass_arg.upper()

    compile_str3 = ''

    for i, s in enumerate(pass_arg):
        if i == 0:
            compile_str3 += s.upper()
        else:
            compile_str3 += s

    compile_str4 = '.' + pass_arg + '.'

    re1 = re.compile(compile_str1)
    re2 = re.compile(compile_str2)
    re3 = re.compile(compile_str3)
    re4 = re.compile(compile_str4)

    match = re1.match(alt_arg) or re2.match(alt_arg) or re3.match(alt_arg) or re4.match(alt_arg)

    if match:
        print('ok')
    else:
        print('nah')


# --------------------------------------------------
main()
