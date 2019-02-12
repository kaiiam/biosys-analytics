#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) < 1:
    print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

in_arg = args[0]

if not os.path.isfile(in_arg):
    print('{} is not a file'.format(in_arg))
    sys.exit(1)

if len(args) >= 2:
    max_count = int(args[1])
else:
    max_count = 3
    

if max_count <= 0:
        print('lines ({}) must be a positive number'.format(max_count))
        sys.exit(1)

with open (in_arg, 'r') as in_file:
    for count, line in enumerate(in_file, start=1):
        if count==max_count:
            print('{}'.format(line[:-1]))
            break
        else:
            print('{}'.format(line[:-1]))



#print(max_count)


#print('Arg is "{}"'.format(arg))
