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
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open('input.txt') as file:
        passports = file.read().split('\n\n')

        count = 0

        for p in passports:
            akeys = [a.split(':')[0] for a in p.split()]

            if sum(akeys.count(k) > 0 for k in keys) != 7:
                continue

            elements = [a.split(':') for a in p.split()]

            ok = True
            for e in elements:
                a = e[1]
                if e[0] == 'byr':
                    if not 1920 <= int(a) <= 2002:
                        ok = False
                if e[0] == 'iyr':
                    if not 2010 <= int(a) <= 2020:
                        ok = False
                if e[0] == 'eyr':
                    if not 2020 <= int(a) <= 2030:
                        ok = False
                if e[0] == 'hgt':
                    #print(a[-2:], a[:-2])
                    if a[-2:] == 'in':
                        if not 59 <= int(a[:-2]) <= 76:
                            ok = False
                    elif a[-2:] == 'cm':
                        if not 150 <= int(a[:-2]) <= 193:
                            ok = False
                    else:
                        ok = False
                if e[0] == 'hcl':
                    if len(a) != 7:
                        ok = False
                    if a[0] != '#':
                        ok = False
                    if not all(e in "01234567890abcdef" for e in a[1:]):
                        ok = False
                if e[0] == 'ecl':
                    if a not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        ok = False
                if e[0] == 'pid':
                    if len(a) != 9 or not a.isnumeric():
                        ok = False

                if not ok:
                    break
            if not ok:
                continue

            count += 1

        print(count)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()