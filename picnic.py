#!/usr/bin/env python3
"""docstring"""

import os
import sys

items = sys.argv[1:]


def main():
   items = []

   while(True):
      item = input('What are you bringing? ["quit" to quit] ')
      items.append(item)
      if item == 'quit':
         break
      print('You are bringing {}'.format(items))
main()
