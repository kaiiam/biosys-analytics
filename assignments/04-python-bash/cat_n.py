#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

in_arg = args[0]

if not os.path.isfile(in_arg):
    print('{} is not a file'.format(in_arg))
    sys.exit(1)

with open (in_arg, 'r') as in_file:
    for count, line in enumerate(in_file, start=1):
        print(' {}: {}'.format(count, line[:-1]))

#print('Arg is "{}"'.format(arg))
