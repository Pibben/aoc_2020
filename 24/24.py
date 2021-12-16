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
        lines = file.read().splitlines()

        #  nw   ne                (-1, -1)   (0, -1)
        # w   o   e           (-1, 0)      o       (1, 0)
        #  sw   se                  (0, 1)   (1, 1)

        map = {'nw': (-1, -1),
               'ne': (0, -1),
               'e': (1, 0),
               'se': (1, 1),
               'sw': (0, 1),
               'w': (-1, 0)}

        grid = {}

        def step(a, b):
            return a[0] + b[0], a[1] + b[1]

        def do(curr, c):
            return step(curr, map[c])

        for line in lines:
            current = (0, 0)
            line = collections.deque(line)
            while line:
                c = line.popleft()
                if c == 'e':
                    current = do(current, 'e')
                if c == 'w':
                    current = do(current, 'w')
                if c == 'n':
                    c2 = line.popleft()
                    current = do(current, 'n' + c2)
                if c == 's':
                    c2 = line.popleft()
                    current = do(current, 's' + c2)

            #print(current)

            if current in grid:
                grid[current] = not grid[current]
            else:
                grid[current] = True

        print(sum(grid.values()))


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        #  nw   ne                (-1, -1)   (0, -1)
        # w   o   e           (-1, 0)      o       (1, 0)
        #  sw   se                  (0, 1)   (1, 1)

        map = {'nw': (-1, -1),
               'ne': (0, -1),
               'e': (1, 0),
               'se': (1, 1),
               'sw': (0, 1),
               'w': (-1, 0)}

        ns = map.values()

        grid = {}

        def step(a, b):
            return a[0] + b[0], a[1] + b[1]

        def do(curr, c):
            return step(curr, map[c])

        for line in lines:
            current = (0, 0)
            line = collections.deque(line)
            while line:
                c = line.popleft()
                if c == 'e':
                    current = do(current, 'e')
                if c == 'w':
                    current = do(current, 'w')
                if c == 'n':
                    c2 = line.popleft()
                    current = do(current, 'n' + c2)
                if c == 's':
                    c2 = line.popleft()
                    current = do(current, 's' + c2)

            #print(current)

            if current in grid:
                grid[current] = not grid[current]
            else:
                grid[current] = True

        for i in range(100):
            new = {}

            for (coord, flag) in grid.items():
                new[coord] = flag
                if flag:
                    for nn in ns:
                        n = step(coord, nn)
                        if n not in grid:
                            new[n] = False

            grid = new
            new = {}

            for (coord, flag) in grid.items():
                count = 0

                for nn in ns:
                    n = step(coord, nn)
                    if n in grid and grid[n]:
                        count += 1

                new[coord] = flag

                if flag and (count == 0 or count > 2):
                    new[coord] = False
                if (not flag) and count == 2:
                    new[coord] = True

            grid = new

        result = sum(grid.values())
        print(result)
        assert(result == 3831)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
