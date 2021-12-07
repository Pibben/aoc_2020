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
    def exp(s, p):
        acc = None
        op = None
        while True:
            if p >= len(s):
                break
            if s[p].isnumeric():
                i = int(s[p])
                if acc is None:
                    acc = i
                else:
                    if op == '+':
                        acc += i
                    if op == '*':
                        acc *= i

            elif s[p] == '(':
                i, pp = exp(s, p + 1)
                if op == '+':
                    acc += i
                elif op == '*':
                    acc *= i
                elif op is None:
                    acc = i

                p = pp

            elif s[p] == ')':
                #print(s, p, acc)
                return acc, p

            elif s[p] == '+':
                op = '+'
            elif s[p] == '*':
                op = '*'

            p += 1

        #print(s, p, acc)
        return acc, p

    with open('input') as file:
        lines = file.read().splitlines()

        sum = 0
        for line in lines:
            line = line.replace(' ', '')
            sum += exp(line, 0)[0]

        print(sum)
        assert(sum == 98621258158412)


def f02():
    def do(a, b, op):
        if op == '+':
            return a + b
        elif op == '*':
            return a * b
        assert False

    def exp(s, p):
        nstack = []
        opstack = []

        while True:
            if p >= len(s):
                break

            if s[p].isnumeric():
                nstack.append(int(s[p]))
            elif s[p] == '+':
                while opstack and opstack[-1] == '+':
                    opstack.pop()
                    nstack.append(nstack.pop() + nstack.pop())
                opstack.append('+')
            elif s[p] == '*':
                while opstack and opstack[-1] != '(':
                    op = opstack.pop()
                    nstack.append(do(nstack.pop(), nstack.pop(), op))
                opstack.append('*')
            elif s[p] == '(':
                opstack.append(s[p])
            elif s[p] == ')':
                while opstack[-1] != '(':
                    op = opstack.pop()
                    assert(opstack)
                    nstack.append(do(nstack.pop(), nstack.pop(), op))
                op = opstack.pop()
                assert(op == '(')

            p += 1

        while opstack:
            op = opstack.pop()
            nstack.append(do(nstack.pop(), nstack.pop(), op))

        return nstack[0], p

    with open('input') as file:
        lines = file.read().splitlines()

        sum = 0
        for line in lines:
            line = line.replace(' ', '')
            sum += exp(line, 0)[0]

        print(sum)
        assert(sum == 241216538527890)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
