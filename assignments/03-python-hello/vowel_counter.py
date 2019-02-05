#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg = args[0]

print('Arg is "{}"'.format(arg))
