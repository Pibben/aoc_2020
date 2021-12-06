import collections
import copy

import numpy as np
import re
import itertools
import functools
import scipy
import scipy.signal


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
    with open('input.txt') as file:
        content = file.read()
        lines = content.splitlines()

        height = len(lines)
        width = len(lines[0])

        data = [a for a in content if a != '\n']
        data = [1 if a == '#' else 0 for a in data]
        a = np.array(data, dtype=np.int32).reshape((1, width, height))

        k = np.ones((3, 3, 3), dtype=np.int32)
        k[1, 1, 1] = 0

        e = np.zeros((3, 3, 3), dtype=np.int32)
        e[1, 1, 1] = 1

        for _ in range(6):
            r = scipy.signal.convolve(a, k, 'full')
            a = scipy.signal.convolve(a, e, 'full')

            a[(a == 1) & ((r < 2) | (r > 3))] = 0
            a[(a == 0) & (r == 3)] = 1

        result = np.sum(a)
        assert(result == 313)
        print(result)


def f02():
    with open('input.txt') as file:
        content = file.read()
        lines = content.splitlines()

        height = len(lines)
        width = len(lines[0])

        data = [a for a in content if a != '\n']
        data = [1 if a == '#' else 0 for a in data]
        a = np.array(data, dtype=np.int32).reshape((1, 1, width, height))

        k = np.ones((3, 3, 3, 3), dtype=np.int32)
        k[1, 1, 1, 1] = 0

        e = np.zeros((3, 3, 3, 3), dtype=np.int32)
        e[1, 1, 1, 1] = 1

        for _ in range(6):
            r = scipy.signal.convolve(a, k, 'full')
            a = scipy.signal.convolve(a, e, 'full')

            a[(a == 1) & ((r < 2) | (r > 3))] = 0
            a[(a == 0) & (r == 3)] = 1

        result = np.sum(a)
        assert(result == 2640)
        print(result)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
