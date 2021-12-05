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
        lines = file.read().splitlines()

        mem = {}

        for line in lines:
            key, val = line.split(" = ")
            if key == "mask":
                om = int(''.join('1' if a == '1' else '0' for a in val), 2)
                am = int(''.join('0' if a == '0' else '1' for a in val), 2)

            else:
                val = int(val)
                addr = int(key[4:-1])
                val &= am
                val |= om
                mem[addr] = val

        result = sum(mem.values())
        assert(result == 15403588588538)
        print(result)


def gen(a, m):

    for i in range(len(a)):
        c = m[i]
        if c == '1':
            a[i] = '1'

    if m.count('X') == 0:
        return [a]
    r = []

    for i in range(len(a)):
        c = m[i]
        if c == 'X':
            mm = m.copy()
            mm[i] = '0'
            a0 = a.copy()
            a0[i] = '0'
            r.extend(gen(a0, mm))
            a1 = a.copy()
            a1[i] = '1'
            r.extend(gen(a1, mm))
            break

    assert(len(r) == 2**m.count('X'))

    return r


def list_to_int(l):
    return int(''.join(l), 2)


def int_to_list(i):
    return list("{0:b}".format(i).zfill(36))


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        mem = {}

        for line in lines:
            key, val = line.split(" = ")
            if key == "mask":
                mask = list(val)

            else:
                val = int(val)
                addr = int_to_list(int(key[4:-1]))

                addrs = gen(addr, mask)

                for a in addrs:
                    a = list_to_int(a)
                    mem[a] = val

        result = sum(mem.values())
        assert(result == 3260587250457)
        print(result)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
