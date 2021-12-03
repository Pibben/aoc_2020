import collections

import numpy as np
import re


def toInt(c):
    return [int(e) for e in c]


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

        lines = toInt(lines)

        preamble_len = 25

        fifo = collections.deque([0] * preamble_len)

        for e in lines[:preamble_len]:
            fifo.appendleft(e)

        lines = lines[preamble_len:]

        def find_pair(num):
            for a in fifo:
                for b in fifo:
                    if a + b == num and a != b:
                        return True
            return False

        for line in lines:
            if not find_pair(line):
                print(line)
                return

            fifo.pop()
            fifo.appendleft(line)


def f02():
    to_find = 1212510616

    with open('input') as file:
        lines = file.read().splitlines()

        lines = toInt(lines)

        fifo = collections.deque([])

        for line in lines:
            if sum(fifo) < to_find:
                fifo.appendleft(line)
            if sum(fifo) == to_find:
                fifo = sorted(fifo)
                print(fifo[0] + fifo[-1])
                return
            while sum(fifo) > to_find:
                fifo.pop()


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()