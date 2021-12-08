import collections
import copy

import numpy as np
import re
import itertools
import functools


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
    with open('input2') as file:
        rules, tests = file.read().split('\n\n')

        d = {}
        for rule in rules.splitlines():
            num, rest = rule.split(': ')
            num = int(num)
            if rest[0] == '"':
                d[num] = rest[1]
                continue
            foo = []
            for r in rest.split('|'):
                for n in r.strip().split(' '):
                   foo.append(int(n))
            d[num] = foo

        print(d)

        def match(n):
            c = d[n]

            if c == 'a' or c == 'b':
                return c

            if len(c) == 1:
                return match(c[0])

            if len(c) == 2:
                return [match(c[0]) + match(c[1])]
            if len(c) == 3:
                return [match(c[0]) + match(c[1]) + match(c[2])]
            if len(c) == 4:
                return [(match(c[0]) + match(c[1])), (match(c[2]) + match(c[3]))]

        print(match(0))


def f02():
    pass


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
