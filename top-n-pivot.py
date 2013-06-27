#!/usr/bin/env python

import sys
from random import randint

def gen_sample(size=1000, lower_bound=0, upper_bound=1000, n_max=10):
    array = [randint(lower_bound, upper_bound) for x in xrange(0, size)]
    replaced = []
    max_list = []
    while len(replaced) < n_max:
        replace_index = randint(0, size)
        if replace_index not in replaced:
            max_item = randint(upper_bound+1, upper_bound+n_max)
            array[replace_index] = max_item
            max_list.append(max_item)
            replaced.append(replace_index)
    return array, max_list

def is_correct(max_array, largest):
    return max_array.sort() == largest.sort()

def run_test(n_max=10):
    array, max_array = gen_sample(size=1000, upper_bound=1000, n_max=n_max)
    largest = find_max(array, n_max=n_max)
    if is_correct(max_array, largest):
        print "Solution Correct :)"
    else:
        print "Solution Incorrect :("

def find_max(array, n_max=1):
    min_index = 0
    max_index = len(array)-1
    pivot = randint(0, max_index)
    i = min_index
    j = max_index

    while True:
        while array[j] > array[pivot]:
            j -= 1
        while array[i] < array[pivot]:
            i += 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        

def main(args):
    n_max = int(args[0])
    run_test(n_max=n_max)

if (__name__ == '__main__'):
    main(sys.argv[1:])
