#!/usr/bin/env python3
"""docstring"""

import os
import sys

#d = {'q1': 'name', 'q2': 'quest', 'q3': 'color'}


#for thing in d:
#    print(d.values())

answers = {}

for thing in ['a', 'b', 'c']:
    answer = input('What is your {}'.format(thing))
    print(answer)
    answers[thing] = answer

print(answers)
