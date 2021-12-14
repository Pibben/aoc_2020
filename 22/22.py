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
        players = file.read().split('\n\n')

        p1 = collections.deque()
        p2 = collections.deque()
        ps = (p1, p2)

        for p in range(2):
            lines = players[p].splitlines()[1:]
            for num in toInt(lines):
                ps[p].append(num)

        while p1 and p2:
            c1, c2 = p1.popleft(), p2.popleft()

            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

        end = p1 if p1 else p2
        score = sum(a * b for (a, b) in zip(reversed(end), range(1, len(end) + 1)))
        print(score)
        assert(score == 32783)


def f02():
    with open('input') as file:
        players = file.read().split('\n\n')

        p1 = collections.deque()
        p2 = collections.deque()
        ps = (p1, p2)

        for p in range(2):
            lines = players[p].splitlines()[1:]
            for num in toInt(lines):
                ps[p].append(num)

        def slice(d, end):
            return collections.deque(list(d)[:end])

        def play(p1, p2):

            history = set()
            while p1 and p2:
                if (tuple(p1), tuple(p2)) in history:
                    return True, p1
                history.add((tuple(p1), tuple(p2)))

                c1, c2 = p1.popleft(), p2.popleft()

                if c1 <= len(p1) and c2 <= len(p2):
                    player1wins, _ = play(slice(p1, c1), slice(p2, c2))
                else:
                    player1wins = c1 > c2

                if player1wins:
                    p1.append(c1)
                    p1.append(c2)
                else:
                    p2.append(c2)
                    p2.append(c1)

            if p1:
                return True, p1
            else:
                return False, p2

        _, end = play(p1, p2)
        score = sum(a * b for (a, b) in zip(reversed(end), range(1, len(end) + 1)))
        print(score)
        assert(score == 33455)



def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
