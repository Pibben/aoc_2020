import collections
import copy

import numpy as np
import re
import itertools
import functools


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
    with open('input.txt') as file:
        card_key, door_key = toInt(file.read().splitlines())

        def do_loop(subject, num):
            curr = 1
            for i in range(num):
                curr *= subject
                curr %= 20201227
            return curr

        def search_loop(subject, target):
            curr = 1
            for i in range(1, 100000000):
                curr *= subject
                curr %= 20201227

                if curr == target:
                    return i

            assert False


        card_loop = search_loop(7, card_key)
        door_loop = search_loop(7, door_key)

        card_enc_key = do_loop(card_key, door_loop)
        door_enc_key = do_loop(door_key, card_loop)

        assert(card_enc_key == door_enc_key)
        print(card_enc_key)


def f02():
    pass


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
