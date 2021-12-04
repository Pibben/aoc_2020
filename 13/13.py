import collections
import copy

import numpy as np
import re
import itertools


def toInt(c):
    return [int(e) for e in c]


def toList(c):
    return [list(r) for r in c]


def msplit(s, ds=None):

    if ds is None:
        ds = ' '

    patt = '|'.join(ds)
    res = re.split(patt, s)
    res = [e for e in res if e != '']
    res = [int(e) if e.isnumeric() else e for e in res]

    return res


def f01():
    with open('input') as file:
        ts, buses = file.read().splitlines()
        ts = int(ts)
        buses = buses.split(',')
        buses = [int(b) for b in buses if b.isnumeric()]

        diff = [-(ts % b) + b for b in buses]
        idx = diff.index(min(diff))
        print(buses[idx] * diff[idx])


def f02():
    with open('input') as file:
        _, buses = file.read().splitlines()

        buses = buses.split(',')
        d = 1
        diff = []

        for i in range(1, len(buses)):
            if buses[i] != 'x':
                diff.append(d)
                d = 1
            else:
                d += 1

        #print(diff)

        buses = [int(b) for b in buses if b.isnumeric()]

        #print(buses)

        for i in itertools.count():
            foo = [(-(i % b) + b) % b for b in buses]
            bar = [foo[j + 1] - foo[j] for j in range(len(buses) - 1)]
            #print(i, foo, bar, diff)
            if foo[0] == 0 and bar == diff:
                print(i)
                break


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()