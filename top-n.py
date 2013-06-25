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

def heapify(array, index, length):
    l = 2*index+1
    r = 2*index+2
    if l < length and array[l] < array[index]:
        smallest = l
    else:
        smallest = index

    if r < length and array[r] < array[smallest]:
        smallest = r

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        heapify(array, smallest, length)

def build_heap(array, length):
    for i in xrange(length/2, 0, -1):
        heapify(array, i-1, length)

def find_max(array, n_max=1):
    build_heap(array, n_max)
    for i in xrange(n_max, len(array)):
        if array[i] > array[0]:
            array[0], array[i] = array[i], array[0]
            heapify(array, 0, n_max)
    return array[0:n_max]

def main(args):
    n_max = int(args[0])
    for i in xrange(10):
        run_test(n_max=n_max)

if (__name__ == '__main__'):
    main(sys.argv[1:])
