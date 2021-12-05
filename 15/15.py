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


def do(num):
    with open('input') as file:
        start = file.read()[:-1]
        nums = toInt(start.split(','))

        mem = {}
        for i, n in enumerate(nums[:-1]):
            mem[n] = i
            last = nums[-1]

        for i in range(len(nums) - 1, num - 1):
            if last in mem:
                last2 = i - mem[last]
            else:
                last2 = 0

            mem[last] = i
            last = last2

        return last


def f01():
    result = do(2020)
    assert(result == 1325)
    print(result)


def f02():
    result = do(30000000)
    assert(result == 59006)
    print(result)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
