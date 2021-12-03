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
        lines = file.read().splitlines()

        ops = []
        for line in lines:
            op, num = line.split()
            num = int(num)
            ops.append((op, num, False))

        ip = 0
        acc = 0

        while True:
            op, num, run = ops[ip]
            if run:
                print(acc)
                return

            ops[ip] = (op, num, True)

            if op == 'nop':
                ip += 1
            if op == 'acc':
                acc += num
                ip += 1
            if op == 'jmp':
                ip += num


def f02():
    with open('input.txt') as file:
        lines = file.read().splitlines()

        ops = []
        for line in lines:
            op, num = line.split()
            num = int(num)
            ops.append((op, num, False))

        def test():

            for j in range(len(ops)):
                op, num, run = ops[j]
                ops[j] = (op, num, False)

            ip = 0
            acc = 0

            while True:
                #print(ip)
                if ip >= len(ops):
                    break
                op, num, run = ops[ip]
                if run:
                    break

                ops[ip] = (op, num, True)

                if op == 'nop':
                    ip += 1
                if op == 'acc':
                    acc += num
                    ip += 1
                if op == 'jmp':
                    ip += num

            if ip == len(ops):
                return True, acc
            else:
                return False, acc

        for i in range(len(ops)):
            op, num, run = ops[i]
            if op == 'jmp':
                ops[i] = ('nop', num, run)
                ok, acc = test()
                #print(i, ok)
                if ok:
                    print(acc)
                    return
                ops[i] = (op, num, run)
            if op == 'nop' and num != 0:
                ops[i] = ('jmp', num, run)
                ok, acc = test()
                #print(i, ok)
                if ok:
                    print(acc)
                    return
                ops[i] = (op, num, run)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()