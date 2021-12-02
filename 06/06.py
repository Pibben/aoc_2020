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
    with open('input') as file:
        groups = file.read().split('\n\n')

        sum = 0

        for group in groups:
            p = group.splitlines()
            s = set()
            for e in p:
                for ee in e:
                    s.add(ee)

            sum += len(s)

        print(sum)


def f02():
    with open('input') as file:
        groups = file.read().split('\n\n')

        sum = 0

        for group in groups:
            p = group.splitlines()
            s = []
            for e in p:
                ss = set()
                for ee in e:
                    ss.add(ee)

                s.append(ss)

            sum += len(set.intersection(*s))

        print(sum)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()