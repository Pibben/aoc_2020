import numpy as np


def toInt(c):
    return [int(e) for e in c]


def f01():
    with open('input.txt') as file:
        values = toInt(file.readlines())
        matches = [(a, b) for a in values for b in values if a + b == 2020]
        print(matches[0][0] * matches[0][1])


def f02():
    with open('input.txt') as file:
        values = toInt(file.readlines())
        matches = [(a, b, c) for a in values for b in values for c in values if a + b + c == 2020]
        print(matches[0][0] * matches[0][1] * matches[0][2])


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()