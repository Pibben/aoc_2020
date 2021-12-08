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
    with open('input') as file:
        rules, tests = file.read().split('\n\n')

        d = {}
        for rule in rules.splitlines():
            num, rest = rule.split(': ')
            num = int(num)
            if rest[0] == '"':
                d[num] = rest[1]
                continue
            foo = []
            for r in rest.split('|'):
                bar = []
                for n in r.strip().split(' '):
                    bar.append(int(n))
                foo.append(bar)
            d[num] = foo

        #print(d)

        def match(s, n):
            if (s, n) in match.m:
                return match.m[(s, n)]

            c = d[n]

            def do(c1, c2):
                #assert(len(s) >= 2)
                if len(s) == 1:
                    return False
                for l in range(1, len(s)):
                    r1 = match(s[:l], c1)
                    if r1:
                        r2 = match(s[l:], c2)

                        if r2:
                            #print(s, c1, c2, "True")
                            return True

               # print(s, c1, c2, "False")
                return False

            if c == 'a' or c == 'b':
                #print(s, n, "True" if s == c else "False")
                result = len(s) == 1 and s == c
                match.m[(s, n)] = result
                return result

            if len(c) == 1:
                if len(c[0]) == 1:
                    # One single
                    result = match(s, c[0][0])
                    match.m[(s, n)] = result
                    return result
                else:
                    # Two and
                    assert(len(c[0]) == 2)
                    result = do(c[0][0], c[0][1])
                    match.m[(s, n)] = result
                    return result

            if len(c) == 2:
                if len(c[0]) == 1:
                    # Two single
                    assert(len(c[1]) == 1)
                    result = match(s, c[0][0]) or match(s, c[1][0])
                    match.m[(s, n)] = result
                    return result
                else:
                    # Two and
                    assert (len(c[1]) == 2)
                    assert (len(c[1]) == 2)
                    result = do(c[0][0], c[0][1]) or do(c[1][0], c[1][1])
                    match.m[(s, n)] = result
                    return result

            assert(False)
        match.m = {}

        print(sum(match(t, 0) for t in tests.splitlines()))

        #for t in tests.splitlines():
            #print(t, match(t, 0))


def f02():
    with open('input') as file:
        rules, tests = file.read().split('\n\n')

        d = {}
        for rule in rules.splitlines():
            num, rest = rule.split(': ')
            num = int(num)
            if rest[0] == '"':
                d[num] = rest[1]
                continue
            foo = []
            for r in rest.split('|'):
                bar = []
                for n in r.strip().split(' '):
                    bar.append(int(n))
                foo.append(bar)
            d[num] = foo

        #print(d)

        def match(s, n):
            if (s, n) in match.m:
                return match.m[(s, n)]

            c = d[n]

            def do(c1, c2):
                #assert(len(s) >= 2)
                if len(s) == 1:
                    return False
                for l in range(1, len(s)):
                    r1 = match(s[:l], c1)
                    if r1:
                        r2 = match(s[l:], c2)

                        if r2:
                            #print(s, c1, c2, "True")
                            return True

               # print(s, c1, c2, "False")
                return False

            def do3(c1, c2, c3):
                #assert(len(s) >= 2)
                if len(s) == 2:
                    return False
                for l in range(1, len(s)):
                    for k in range(l + 1, len(s)):
                        #print(s, s[:l], s[l:k], s[k:])
                        r1 = match(s[:l], c1)
                        if r1:
                            r2 = match(s[l:k], c2)

                            if r2:
                                r3 = match(s[k:], c3)
                                #print(s, c1, c2, "True")
                                if r3:
                                    return True

               # print(s, c1, c2, "False")
                return False

            if n == 8:
                return match(s, 42) or do(42, 8)

            if n == 11:
                return do(42, 31) or do3(42, 11, 31)

            if c == 'a' or c == 'b':
                #print(s, n, "True" if s == c else "False")
                result = len(s) == 1 and s == c
                match.m[(s, n)] = result
                return result

            if len(c) == 1:
                if len(c[0]) == 1:
                    # One single
                    result = match(s, c[0][0])
                    match.m[(s, n)] = result
                    return result
                else:
                    # Two and
                    assert(len(c[0]) == 2)
                    result = do(c[0][0], c[0][1])
                    match.m[(s, n)] = result
                    return result

            if len(c) == 2:
                if len(c[0]) == 1:
                    # Two single
                    assert(len(c[1]) == 1)
                    result = match(s, c[0][0]) or match(s, c[1][0])
                    match.m[(s, n)] = result
                    return result
                else:
                    # Two and
                    assert (len(c[1]) == 2)
                    assert (len(c[1]) == 2)
                    result = do(c[0][0], c[0][1]) or do(c[1][0], c[1][1])
                    match.m[(s, n)] = result
                    return result

            assert(False)
        match.m = {}

        print(sum(match(t, 0) for t in tests.splitlines()))

        #for t in tests.splitlines():
            #print(t, match(t, 0))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
