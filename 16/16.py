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
        rules, my, near = file.read().split('\n\n')

        rules = rules.splitlines()
        my = my.splitlines()[1]
        near = near.splitlines()[1:]

        limits = []
        for r in rules:
            name, limit1, limit2 = msplit(r, [': ', ' or '])
            limits.append((toInt(limit1.split('-')), toInt(limit2.split('-'))))

        sum = 0

        for nn in near:
            for n in toInt(nn.split(',')):
                valid = False
                for l in limits:
                    if (l[0][0] <= n <= l[0][1]) or (l[1][0] <= n <= l[1][1]):
                        valid = True
                        break
                if not valid:
                    sum += n

        assert(sum == 19060)
        print(sum)


def mbm(c):
    a = range(len(c))
    b = list(set.union(*c))

    def do(u, matches, seen):
        for v in c[u]:
            vi = b.index(v)
            if not seen[vi]:
                seen[vi] = True
                if matches[vi] is None or do(matches[vi], matches, seen):
                    matches[vi] = u
                    return True
        return False

    matches = [None] * len(b)
    for u in a:
        do(u, matches, [False] * len(b))

    return [b[matches.index(aa)] for aa in a]


def f02():
    with open('input') as file:
        rules, my, near = file.read().split('\n\n')

        rules = rules.splitlines()
        my = toInt(my.splitlines()[1].split(','))
        near = near.splitlines()[1:]

        limits = []
        departure = []
        for r in rules:
            name, limit1, limit2 = msplit(r, [': ', ' or '])
            if name.startswith('departure'):
                departure.append(name)
            limits.append((toInt(limit1.split('-')), toInt(limit2.split('-')), name))

        def is_valid(t):
            for n in toInt(t.split(',')):
                valid = False
                for l in limits:
                    if (l[0][0] <= n <= l[0][1]) or (l[1][0] <= n <= l[1][1]):
                        valid = True
                        break
                if not valid:
                    return False

            return True

        valid_near = [n for n in near if is_valid(n)]

        names = []
        for f in range(len(rules)):
            names.append(set())
            for ri in range(len(rules)):
                l = limits[ri]
                ok = True
                for n in valid_near:
                    n = toInt(n.split(','))[f]
                    if not ((l[0][0] <= n <= l[0][1]) or (l[1][0] <= n <= l[1][1])):
                        ok = False
                        break
                if ok:
                    names[f].add(l[2])

        actual = mbm(names)

        indices = [actual.index(a) for a in departure]

        result = functools.reduce((lambda x, y: x * y), [my[a] for a in indices])
        print(result)
        assert(result == 953713095011)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
