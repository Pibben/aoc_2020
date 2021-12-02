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
    with open('input.txt') as file:
        rows = file.read().splitlines()
        width = len(rows[0])

        count = 0
        x = 0

        for row in rows:
            if row[x % width] == '#':
                count += 1

            x += 3

        print(count)


def f02():
    with open('input.txt') as file:
        rows = file.read().splitlines()
        width = len(rows[0])

    def slope(xstep, ystep):
        count = 0
        x = 0
        y = 0

        while y < len(rows):
            if rows[y][x % width] == '#':
                count += 1

            x += xstep
            y += ystep

        return count

    print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()