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
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open('input.txt') as file:
        passports = file.read().split('\n\n')

        count = 0

        for p in passports:
            akeys = [a.split(':')[0] for a in p.split()]

            if sum(akeys.count(k) > 0 for k in keys) == 7:
                count += 1

    print(count)


def f02():
    verify = [('byr', lambda a : 1920 <= int(a) <= 2002),
              ('iyr', lambda a : 2010 <= int(a) <= 2020),
              ('eyr', lambda a : 2020 <= int(a) <= 2030),
              ('hgt', lambda a : 59 <= int(a[:-2]) <= 76 if a[-2:] == 'in' else 150 <= int(a[:-2]) <= 193),
              ('hcl', lambda a : a[0] == '#' and 
              'ecl',
              'pid']

    with open('input.txt') as file:
        passports = file.read().split('\n\n')

        count = 0

        for p in passports:
            elements = [a.split(':') for a in p.split()]

            for e in elements:
                if e[0] == 'byr':


            if sum(akeys.count(k) > 0 for k in keys) == 7:
                count += 1

    print(count)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()