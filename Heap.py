#!/usr/bin/env python

import sys

class Heap(object):
    def __init__(self, values):
        self.values = values
        self.build_heap()

    def build_heap(self):
        self.size = len(self.values)
        for i in xrange(len(self.values), 0, -1):
            self.heapify(i-1)

    def parent(self, node):
        if not node:
            return None
        else:
            return (node-1)/2

    def left(self, node):
        return 2*node+1

    def right(self, node):
        return 2*node+2

    def heapify(self, node):
        l = self.left(node)
        r = self.right(node)
        if l < self.size and self.values[l] > self.values[node]:
            largest = l
        else:
            largest = node
        
        if r < self.size and self.values[r] > self.values[largest]:
            largest = r
        
        if largest != node:
            self.values[node], self.values[largest] = self.values[largest], self.values[node]
            self.heapify(largest)

    def sort(self):
        for i in xrange(len(self.values)-1, 0, -1):
            self.values[i], self.values[0] = self.values[0], self.values[i]
            self.size -= 1
            self.heapify(0)

    def __unicode__(self):
        return "{}".format(self.values)

def main(args):
    l = [1, 3, 4, 10, 9, 2, 17]
    h = Heap(l)
    print h.values
    h.sort()
    print h.values
    h.build_heap()
    print h.values
    h.sort()
    print h.values

if (__name__ == '__main__'):
    main(sys.argv[1:])
