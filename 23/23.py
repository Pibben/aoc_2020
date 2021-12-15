import collections
import copy

import numpy as np
import re
import itertools
import functools
import pprint


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
        start = toInt(list(file.readline()[:-1]))
        max_num = max(start)
        min_num = min(start)

        for _ in range(100):
            current = start[0]
            pick = start[1:4]
            rest = start[4:]
            dst_label = current - 1
            while dst_label not in rest:
                dst_label -= 1
                if dst_label < min_num:
                    dst_label = max_num
            dst_idx = rest.index(dst_label) + 1

            new = rest[:dst_idx] + pick + rest[dst_idx:] + [current]
            start = new

        idx = start.index(1)
        result = start[idx:] + start[:idx]
        result = ''.join(str(i) for i in result[1:])
        print(result)
        assert(result == '62934785')


def f02():
    pass


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
