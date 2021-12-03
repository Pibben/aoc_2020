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
        lines = sorted(toInt(lines))

        a = np.array(lines)
        a = np.insert(a, 0, 0)
        a = np.append(a, a[-1] + 3)
        d = np.diff(a)
        print(np.count_nonzero(d == 1) * np.count_nonzero(d == 3))
        #print(d)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()
        lines = sorted(toInt(lines))
        lines.insert(0, 0)

        target = lines[-1] + 3

        lines.append(target)

        def count(idx):
            if count.cache[idx] is not None:
                return count.cache[idx]

            if idx == len(lines) - 1:
                return 1

            sum = 0
            for i in range(1, 4):
                if idx + i < len(lines) and lines[idx + i] - lines[idx] <= 3:
                    sum += count(idx + i)

            count.cache[idx] = sum
            return sum
        count.cache = [None] * len(lines)

        print(count(0))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()