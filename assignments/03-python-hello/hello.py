#!/usr/bin/env python3
"""docstring"""

import os
import sys

names = sys.argv[1:]

if len(names) == 0:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if len(names) == 1:
   print('Hello to the 1 of you '+names[0]+'!' )
elif len(names) == 2:
   print('hello ... {}'.format(' and '.join(names)))

print('Names is "{}"'.format(names))
