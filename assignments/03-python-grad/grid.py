#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

num = int(args[0])

#print('Arg is "{}"'.format(num))

if num not in range(2,10):
    print("NUM ({}) must be between 1 and 9".format(num))
    sys.exit(1)

#print(num**2)

# answer 3 from the following link was super helpful
#https://stackoverflow.com/questions/29882428/how-to-print-a-list-of-lists-in-a-grid-format

for count, x in enumerate(range(1,num**2 +1)):
    print('{0:3}'.format(x), end='')
    if (count+1)%num == 0:
        print('')

    #print((count+1)%num)
