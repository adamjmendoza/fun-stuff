#!/usr/bin/env python

import sys

def find_start_index(peaks):
    highest = 0
    for i in xrange(1, len(peaks)):
        if peaks[i] < peaks[highest]:
            return highest
        else:
            highest = i
    return highest

def fill(peaks):
    start = find_start_index(peaks)
    current = start+1
    while current < len(peaks) and peaks[current] < peaks[start]:
        current += 1

    if current-start-1 > 1:
        min_index = start+1 if peaks[start+1] <= peaks[current] else current
        volume = reduce(lambda x, y: x+y, map(lambda x: peaks[min_index]-peaks[x], range(start+1, current)))
    else:
        volume = 0
    
    print "[{}, {}] --> {}".format(start, current, volume)
    if current < len(peaks)-1:
        volume += fill(peaks[current:])
    return volume

def main(args):
#    peaks = [1, 4, 3, 2, 1, 2, 1, 3, 4, 5, 4, 3, 6, 2, 1]
    peaks = [2, 1, 3, 1, 2]
    volume = fill(peaks)
    print volume

if (__name__ == '__main__'):
    main(sys.argv[1:])
