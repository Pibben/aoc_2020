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


def parse(s, zero, one):
    s = s.replace(zero, '0')
    s = s.replace(one, '1')
    return int(s, 2)


def f01():
    maxid = 0
    with open('input') as file:
        seats = file.read().splitlines()

        for seat in seats:
            row = parse(seat[:7], 'F', 'B')
            col = parse(seat[7:], 'L', 'R')

            id = row * 8 + col
            maxid = max(id, maxid)

        print(maxid)


def f02():
    with open('input') as file:
        seats = file.read().splitlines()

        ids = []

        for seat in seats:
            row = parse(seat[:7], 'F', 'B')
            col = parse(seat[7:], 'L', 'R')

            ids.append(row * 8 + col)

        ids = sorted(ids)
        for i in range(ids[0], ids[-1]):
            if i not in ids:
                print(i)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()