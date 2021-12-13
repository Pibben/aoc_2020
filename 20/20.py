import collections
import copy
import pprint

import numpy as np
import re
import itertools
import functools
import scipy
import scipy.signal


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


def lines_to_matrix(lines, translation):
    height = len(lines)
    width = len(lines[0])

    r = np.zeros((height, width), dtype=np.int32)

    for y in range(height):
        r[y, :] = [translation[c] for c in lines[y]]

    return r


def extract_edges(tile):
    edge1 = tuple(tile[0, :])    # ^
    edge2 = tuple(tile[:, -1])   # >
    edge3 = tuple(tile[-1, :][::-1])   # v
    edge4 = tuple(tile[:, 0][::-1])    # <

    return [edge1, edge2, edge3, edge4]


def f01():
    with open('input.txt') as file:
        tiles = file.read().split('\n\n')

        db = set()

        for tile in tiles:
            tile = tile.splitlines()
            header = tile[0]
            tile = tile[1:]
            num = int(header[5:-1])

            tile = lines_to_matrix(tile, {'#': 1, '.': 0})

            for t in extract_edges(tile):
                db.add((t, num))

            for t in extract_edges(np.flip(tile, axis=0)):
                db.add((t, num))

            for t in extract_edges(np.flip(tile, axis=1)):
                db.add((t, num))

        prod = 1

        for tile in tiles:
            tile = tile.splitlines()
            header = tile[0]
            tile = tile[1:]
            num = int(header[5:-1])

            tile = lines_to_matrix(tile, {'#': 1, '.': 0})

            count = 0
            for t in extract_edges(tile):
                for e in db:
                    if e[0] == t and e[1] != num:
                        count += 1
            #print(num, count)
            if count == 2:
                prod *= num

        print(prod)
        assert(prod == 20913499394191)


def find_upper_left_corner(tiles):
    db = []
    for tile in tiles:

        for t in extract_edges(tile):
            db.append(t)

        for t in extract_edges(np.flip(tile, axis=0)):
            db.append(t)

        for t in extract_edges(np.flip(tile, axis=1)):
            db.append(t)

    for tile in tiles:
        edges = extract_edges(tile)
        t1, t2 = edges[0], edges[3]
        c1, c2 = db.count(t1), db.count(t2)
        #print(c1, c2)
        if c1 == 1 and c2 == 1:
            return tile


def find_left(tiles, edge, this):
    for tile in tiles:
        if np.array_equal(this, tile):
            continue
        for rot in range(4):
            rt = np.rot90(tile, rot)

            if all(rt[:, 0] == edge):
                return tile, rot, None

            for axis in [0, 1, (0, 1)]:

                rtf = np.flip(rt, axis=axis)

                if all(rtf[:, 0] == edge):
                    return tile, rot, axis

    return None


def find_up(tiles, edge, this):
    #print("Finding", edge)
    for tile in tiles:
        if np.array_equal(this, tile):
            continue
        for rot in range(4):
            rt = np.rot90(tile, rot)

            if all(rt[0, :] == edge):
                return tile, rot, None

            for axis in [0, 1, (0, 1)]:

                rtf = np.flip(rt, axis=axis)

                if all(rtf[0, :] == edge):
                    return tile, rot, axis

    return None


def apply(tile, rot, flip):
    tile = np.rot90(tile, rot)
    if flip is not None:
        tile = np.flip(tile, flip)
    return tile


def erode(tile):
    return tile[1:-1, 1:-1]


def place(tile, rot, flip, tiles, grid, y, x):
    #print(y, x)
    rotflip = apply(tile, rot, flip)
    #pprint.pprint(rotflip)
    grid[y].append((tile, rot, flip))
    edges = extract_edges(rotflip)
    right_result = find_left(tiles, edges[1], tile)
    up_result = find_up(tiles, edges[2][::-1], tile)

    if right_result is not None:
        right, rrot, rflip = right_result
        place(right, rrot, rflip, tiles, grid, y, x + 1)
    if up_result is not None and x == 0:
        grid.append([])
        down, drot, dflip = up_result
        place(down, drot, dflip, tiles, grid, y + 1, x)


def canvas(grid):
    col = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[0])):
            next_tile = apply(*grid[y][x])
            next_tile = next_tile[1:-1, 1:-1]
            row.append(next_tile)
        col.append(np.concatenate(row, axis=1))
    return np.concatenate(col, axis=0)



def f02():
    with open('input.txt') as file:
        tiles = file.read().split('\n\n')

        ntiles = []

        grid = [[]]

        for tile in tiles:
            tile = tile.splitlines()
            tile = tile[1:]

            nptile = lines_to_matrix(tile, {'#': 1, '.': 0})
            ntiles.append(np.flipud(nptile))

        # Position corner tile
        ulc = find_upper_left_corner(ntiles)

        place(ulc, 0, None, ntiles, grid, 0, 0)

        #pprint.pprint(ulc)

        #pprint.pprint(grid)
        c = canvas(grid)

        #pprint.pprint(c)
        #print(c.shape)

        monster = lines_to_matrix(["                  # ",
                                   "#    ##    ##    ###",
                                   " #  #  #  #  #  #   "], {'#': 1, ' ': 0})
        #pprint.pprint(monster)

        for rot in range(4):
            c = np.rot90(c, rot)

            s = scipy.signal.convolve2d(c, monster, 'valid')
            monsters = np.sum(s == np.sum(monster))
            if monsters != 0:
                result = np.sum(c) - monsters * np.sum(monster)
                print(result)

            for axis in [0, 1, (0, 1)]:
                c = np.flip(c, axis)
                s = scipy.signal.convolve2d(c, monster, 'valid')

                monsters = np.sum(s == np.sum(monster))
                if monsters != 0:
                    result = np.sum(c) - monsters * np.sum(monster)
                    print(result)




def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
