#!/usr/bin/env python

import sys

ELEMENTS = ['ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', \
            'b', 'ba', 'be', 'bh', 'bi', 'bk', 'br', \
            'c', 'ca', 'cd', 'ce', 'cf', 'cl', 'cm', 'co', 'cn', 'cr', 'cs', 'cu', \
            'db', 'ds', 'dy', \
            'er', 'es', 'eu', \
            'f', 'fe', 'fm', 'fr', \
            'ga', 'gd', 'ge', \
            'h', 'he', 'hf', 'hg', 'ho', 'hs', \
            'i', 'in', 'ir', \
            'k', 'kr', 'la', 'li', 'lr', 'lu', \
            'md', 'mg', 'mn', 'mo', 'mt', \
            'n', 'na', 'nb', 'nd', 'ne', 'ni', 'no', 'np', 
            'o', 'os', \
            'p', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt', 'pu', \
            'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', \
            's', 'sb', 'sc', 'se', 'sg', 'si', 'sm', 'sn', 'sr', \
            'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', \
            'u', 'uuh', 'uun', 'uuo', 'uup', 'uuq', 'uus', 'uut', 'uuu', \
            'v', \
            'w', \
            'xe', \
            'y', 'yb', \
            'zn', 'zr',]

def is_fragment(fragment, elements=None, solutions=None):
    if not elements:
        elements = []
    if not solutions:
        solutions = []

    for i in range(1, 4):
        if len(fragment) >= i:
            if fragment[0:i] in ELEMENTS:
                if len(fragment[i:]) == 0:
                    solutions.append(elements+[fragment[0:i]])
                else:
                    solutions = is_fragment(fragment[i:], elements+[fragment[0:i]], solutions)
    return solutions
            
def main(args):
    word = args[0]
    elements = is_fragment(word)
    print elements

if (__name__ == '__main__'):
    main(sys.argv[1:])
