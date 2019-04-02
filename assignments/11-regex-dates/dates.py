#!/usr/bin/env python3
"""
Author : kai
Date   : 2019-04-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DATE', help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pos_arg = args.positional

    date_re1 = re.compile('(?P<year>\d{4})'
                     #'[/]?'
                     '[-]?'
                     '\s*'
                     '(?P<month>\d{,2})'
                     #'[/]?'
                     '[-]?'
                     '\s*'
                     '(?P<day>\d{,2})')

    date_re2 = re.compile('(?P<month>\d{,2})'
                        '[/]'
                        '(?P<year>\d{2})')

    date_re3 = re.compile('(?P<month>\w+)'
                        '[-]?'
                        '[,]?'
                        '[\s]?'
                        '(?P<year>\d{4})')


    match1 = date_re1.match(pos_arg)
    match2 = date_re2.match(pos_arg)
    match3 = date_re3.match(pos_arg)

    # print('{}: {}'.format(pos_arg, 'match' if match else 'miss'))

    if match1:
        month = match1.group('month')
        #print(month)
        if month == '':
            print('No match')
            sys.exit(0)
        if len(month) < 2:
            month = '0' + month

        day = match1.group('day')
        if len(day) == 0:
            day = '01'
        if len(day) == 1:
            day = '0' + day
        print('{}-{}-{}'.format(match1.group('year'), month, day ))
        #print(month)
        sys.exit(0)


    if match2:
        month = match2.group('month')

        if len(month) < 2:
            month = '0' + month

        year = match2.group('year')
        if len(year) < 4:
            year = '20' + year

            print('{}-{}-01'.format(year, month))
            sys.exit(0)


    month_lookup = {
                    'jan' : '01',
                    'feb' : '02',
                    'mar' : '03',
                    'apr' : '04',
                    'may' : '05',
                    'jun' : '06',
                    'jul' : '07',
                    'aug' : '08',
                    'sep' : '09',
                    'oct' : '10',
                    'nov' : '11',
                    'dec' : '12'
                  }

    if match3:
        #print(match3.group('month') , match3.group('year'))
        month = match3.group('month').lower()
        #print(month[0:3])
        #print(month_lookup[month[0:3]])
        print('{}-{}-01'.format(match3.group('year'), month_lookup[month[0:3]]))
        sys.exit(0)


    print('No match')


# --------------------------------------------------
if __name__ == '__main__':
    main()
