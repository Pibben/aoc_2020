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

        colormap = {}

        for line in lines:
            color, contents = line[:-1].split(" bags contain ")
            content = contents.split(", ")
            for c in content:
                split = c.split()
                num = split[0]
                ccolor = ' '.join(split[1:-1])
                if ccolor not in colormap:
                    colormap[ccolor] = []
                colormap[ccolor].append(color)

        #print(colormap)

        s = set()

        stack = ['shiny gold']

        while stack:
            current = stack.pop()
            if current in colormap:
                for a in colormap[current]:
                    s.add(a)
                    stack.append(a)

        print(len(s))


def f02():
    with open('input.txt') as file:
        lines = file.read().splitlines()

        colormap = {}

        for line in lines:
            color, contents = line[:-1].split(" bags contain ")
            if contents == 'no other bags':
                colormap[color] = []
                continue
            content = contents.split(", ")
            for c in content:
                split = c.split()
                num = int(split[0])
                ccolor = ' '.join(split[1:-1])
                if color not in colormap:
                    colormap[color] = []
                colormap[color].append((ccolor, num))

        def getSum(color):
            sum = 1
            for ccolor, num in colormap[color]:
                sum += num * getSum(ccolor)

            return sum

        print(getSum('shiny gold') - 1)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()