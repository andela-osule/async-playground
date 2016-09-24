#!/usr/local/bin/python3

# Using the ChainMap class :: performance

from collections import ChainMap
from timeit import timeit

u = {'u': 'John'}
p = {'u': 'John', 'p': 'riley'}
d = ChainMap(u, p)


def dolog():
    print(d['u'])
    print(d['p'])


def dolog1():
    print(u.get('u', p.get('u')))
    print(u.get('p', p.get('p')))

if __name__ == '__main__':
    print(timeit(stmt=dolog, number=1))
    print(timeit(stmt=dolog1, number=1))
