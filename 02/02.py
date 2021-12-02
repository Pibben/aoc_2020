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
        rows = file.readlines()
        count = 0

        for row in rows:
            low, high, char, pw = msplit(row, ['-', ' ', ':'])

            lc = pw.count(char)
            if low <= lc <= high:
                count += 1

        print(count)


def f02():
    with open('input.txt') as file:
        rows = file.readlines()
        count = 0

        for row in rows:
            low, high, char, pw = msplit(row, ['-', ' ', ':'])

            if (pw[low - 1] == char) != (pw[high - 1] == char):
                count += 1

        print(count)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()