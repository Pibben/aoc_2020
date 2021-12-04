import collections
import copy

import numpy as np
import re


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

        pos = [0, 0]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
        diri = 1
        for line in lines:
            op = line[0]
            num = int(line[1:])

            if op == 'N':
                pos[1] += num
            if op == 'E':
                pos[0] += num
            if op == 'S':
                pos[1] -= num
            if op == 'W':
                pos[0] -= num
            if op == 'L':
                assert(num % 90 == 0)
                diri -= num // 90
                diri %= 4
            if op == 'R':
                assert(num % 90 == 0)
                diri += num // 90
                diri %= 4
            if op == 'F':
                pos[0] += dirs[diri][0] * num
                pos[1] += dirs[diri][1] * num

        print(abs(pos[0] + abs(pos[1])))


def f02():
    def rotcw(pos):
        return [pos[1], -pos[0]]

    def rotccw(pos):
        return [-pos[1], pos[0]]

    with open('input') as file:
        lines = file.read().splitlines()

        wp = [10, 1]  # W/E, S/N
        pos = [0, 0]

        for line in lines:
            op = line[0]
            num = int(line[1:])

            if op == 'N':
                wp[1] += num
            if op == 'E':
                wp[0] += num
            if op == 'S':
                wp[1] -= num
            if op == 'W':
                wp[0] -= num
            if op == 'L':
                assert(num % 90 == 0)
                num //= 90
                for _ in range(num):
                    wp = rotccw(wp)
            if op == 'R':
                assert(num % 90 == 0)
                num //= 90
                for _ in range(num):
                    wp = rotcw(wp)
            if op == 'F':
                for _ in range(num):
                    pos[0] += wp[0]
                    pos[1] += wp[1]

        print(abs(pos[0] + abs(pos[1])))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()