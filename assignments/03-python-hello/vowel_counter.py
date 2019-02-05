#!/usr/bin/env python3
"""docstring"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

in_string = args[0]

#print('Arg is "{}"'.format(in_string))

vowel_list = ['a','e','i','o','u','A','E','I','O','U']

vowel_count = 0

for c in in_string:
    if c in vowel_list:
        vowel_count += 1

if vowel_count == 1:
    outstring = 'There is ' + str(vowel_count) + ' vowel in "' + str(in_string) + '."'
else:
    outstring = 'There are ' + str(vowel_count) + ' vowels in "' + str(in_string) + '."'

print(outstring)
