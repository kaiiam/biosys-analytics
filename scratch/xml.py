#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import os
import sys
from xml.etree.ElementTree import ElementTree

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)


    file = args[0]

    print('file is "{}"'.format(file))

    tree = ElementTree()
    root = tree.parse(file)
    print(typeroot.attrib))
    for key, value in root.attrib.items():
        print('{:13}

# --------------------------------------------------
main()
