#!/usr/bin/env python

import sys

def gen_permutations(s):
    a = list(s)
    a.sort()

    j = len(a)
    while j >= 0:
        yield "".join(a)
        j = len(a)-2
        while j >= 0 and a[j] >= a[j+1]:
            j -= 1
        if j >= 0:
            l = len(a)-1
            while a[j] >= a[l]:
                l -= 1
            a[j], a[l] = a[l], a[j]
            a[j+1:] = a[-1:j:-1]

def gen_permutations_recursive(a, i, n):
    if i == n:
        print "".join(a)
        return
    j = i
    while j <= n:
        a[i], a[j] = a[j], a[i]
        gen_permutations_recursive(a, i+1, n)
        a[i], a[j] = a[j], a[i]
        j += 1

def main(args):
    string = args[0]
    print "--------------------- Iterative ---------------------"
    perms = gen_permutations(string)
    for p in perms:
        print p

if (__name__ == '__main__'):
    main(sys.argv[1:])
