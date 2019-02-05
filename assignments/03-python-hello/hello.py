#!/usr/bin/env python3
"""docstring"""

import os
import sys

names = sys.argv[1:]

if len(names) == 0:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

# if len(names) == 1:
#    print('Hello to the 1 of you: '+ names[0]+'!' )
# elif len(names) == 2:
#    print('Hello to the 2 of you: {}'.format(' and '.join(names)))
# elif len(names) == 3:
#    print('Hello to the 3 of you:'+ names[0] + names[1]+ names[2]+ '!' )
#

if len(names) > 1:
    names[-1] = 'and ' + str(names[-1])
    #print(names[-1])

if len(names) == 1:
   print('Hello to the 1 of you: '+ names[0]+'!' )
elif len(names) == 2:
   print('Hello to the 2 of you: {}'.format(' '.join(names)) +'!' )
elif len(names) > 2:
   print('Hello to the ' + str(len(names)) +' of you: {}'.format(', '.join(names)) +'!' )

#print('Names is "{}"'.format(names))
