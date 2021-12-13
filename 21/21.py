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

    return [b[matches.index(aa)] if aa in matches else None for aa in a]


def f01():
    with open('input') as file:
        lines = file.read().splitlines()

        map = []
        key = []
        all_ingredients = []
        for line in lines:
            ingredients, allergens = line.split(' (contains ')
            ingredients = ingredients.split(' ')
            all_ingredients.extend(ingredients)
            allergens = allergens[:-1].split(', ')

            for a in allergens:
                if a not in key:
                    key.append(a)
                    map.append(set(ingredients))
                else:
                    map[key.index(a)] = map[key.index(a)].intersection(set(ingredients))

        matches = mbm(map)

        count = 0
        for i in all_ingredients:
            if i not in matches:
                count += 1

        print(count)
        assert(count == 2317)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        map = []
        key = []
        all_ingredients = []
        for line in lines:
            ingredients, allergens = line.split(' (contains ')
            ingredients = ingredients.split(' ')
            all_ingredients.extend(ingredients)
            allergens = allergens[:-1].split(', ')

            for a in allergens:
                if a not in key:
                    key.append(a)
                    map.append(set(ingredients))
                else:
                    map[key.index(a)] = map[key.index(a)].intersection(set(ingredients))

        matches = mbm(map)
        result = sorted(list(zip(key, matches)))
        result = [r[1] for r in result]
        result = ','.join(result)
        print(result)
        assert(result == 'kbdgs,sqvv,slkfgq,vgnj,brdd,tpd,csfmb,lrnz')


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
