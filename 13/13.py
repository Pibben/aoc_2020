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


def reduce(step1, step2, diff, start):
    for i in range(start, step1 * step2 + start, step2):
        if (i - diff) % step1 == 0:
            return i


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

        buses = [int(b) for b in buses if b.isnumeric()]

        current_step = 1
        result = 0
        for i in range(len(buses) - 2, -1, -1):
            current_step *= buses[i + 1]
            result = reduce(buses[i], current_step, diff[i], result) - diff[i]

        assert(result == 487905974205117)
        print(result)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()