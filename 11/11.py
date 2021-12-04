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
        rows = toList(file.read().splitlines())
        nrows = len(rows)
        ncols = len(rows[0])

        def count_all():
            return sum(sum((c == '#') for c in row) for row in rows)

        def count_occupied(row, col):
            count = 0
            for ro in range(-1, 2):
                for co in range(-1, 2):
                    if ro == 0 and co == 0:
                        continue
                    r = row + ro
                    c = col + co
                    if 0 <= r < nrows and 0 <= c < ncols and rows[r][c] == '#':
                        count += 1
            return count

        changed = True
        while changed:
            changed = False
            new = copy.deepcopy(rows)
            for r in range(nrows):
                for c in range(ncols):

                    cnt = count_occupied(r, c)
                    if rows[r][c] == 'L' and cnt == 0:
                        new[r][c] = '#'
                        changed = True
                    if rows[r][c] == '#' and cnt >= 4:
                        new[r][c] = 'L'
                        changed = True

            rows = copy.deepcopy(new)

        result = count_all()
        assert(result == 2243)
        print(result)


def f02():
    with open('input') as file:
        rows = toList(file.read().splitlines())
        nrows = len(rows)
        ncols = len(rows[0])

        def count_all():
            return sum(sum((c == '#') for c in row) for row in rows)

        def count_occupied(row, col):
            dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

            count = 0
            for d in dirs:
                r = row
                c = col
                rd, cd = d
                while True:
                    r += rd
                    c += cd
                    if r < 0 or r >= nrows or c < 0 or c >= ncols:
                        break
                    if rows[r][c] == '#':
                        count += 1
                        break
                    if rows[r][c] == 'L':
                        break

            return count

        changed = True
        while changed:
            changed = False
            new = copy.deepcopy(rows)
            for r in range(nrows):
                for c in range(ncols):

                    cnt = count_occupied(r, c)
                    if rows[r][c] == 'L' and cnt == 0:
                        new[r][c] = '#'
                        changed = True
                    if rows[r][c] == '#' and cnt >= 5:
                        new[r][c] = 'L'
                        changed = True

            rows = copy.deepcopy(new)

        result = count_all()
        assert(result == 2027)
        print(result)


def main():
    #f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()