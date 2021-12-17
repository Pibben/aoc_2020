import collections
import copy

import numpy as np
import re
import itertools
import functools
import pprint


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


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def link(self, nxt):
        self.next = nxt

    def __str__(self):
        return ' '.join(str(a) for a in self.to_list())

    def cut_right(self, num):
        new_head = self.next
        curr = self
        for i in range(num):
            curr = curr.next
        self.next = curr.next
        curr.next = new_head

        return new_head

    def insert_right(self, new):
        old_next = self.next
        self.next = new
        curr = new
        while curr.next != new:
            curr = curr.next
        assert(curr.next == new)
        curr.next = old_next

    def __len__(self):
        count = 1
        curr = self.next
        while curr != self:
            count += 1
            curr = curr.next
        return count

    def to_list(self):
        curr = self
        ret = []
        while True:
            ret.append(curr.val)
            curr = curr.next
            if curr == self:
                break
        return ret

    def contains(self, key):
        curr = self
        while True:
            if curr.val == key:
                return True
            curr = curr.next
            if curr == self:
                break
        return False


def create_from_list(plist):
    map = {}
    prev = None
    head = None
    n = None
    for e in plist:
        n = Node(e)
        map[e] = n
        if prev is not None:
            prev.link(n)
        prev = n
        if head is None:
            head = n

    if n is not None:
        n.link(head)

    return head, map


def f01():
    with open('input') as file:
        start = toInt(list(file.readline()[:-1]))
        max_num = max(start)
        min_num = min(start)
        length = len(start)

        l, m = create_from_list(start)

        current_label = start[0]

        for _ in range(100):
            pick = m[current_label].cut_right(3)
            dst_label = current_label - 1
            if dst_label < min_num:
                dst_label = max_num
            while pick.contains(dst_label):
                dst_label -= 1
                if dst_label < min_num:
                    dst_label = max_num

            m[dst_label].insert_right(pick)
            assert(len(m[1]) == length)
            current_label = m[current_label].next.val

        result = ''.join(str(i) for i in m[1].to_list()[1:])
        print(result)
        assert(result == '62934785')


def f02():
    with open('input') as file:
        start = toInt(list(file.readline()[:-1]))
        max_num = max(start)
        min_num = min(start)

        start.extend([i for i in range(max_num + 1, 1000001)])

        length = len(start)
        assert(length == 1000000)
        max_num = 1000000

        l, m = create_from_list(start)

        current_label = start[0]

        for _ in range(10*1000*1000):
            pick = m[current_label].cut_right(3)
            dst_label = current_label - 1
            if dst_label < min_num:
                dst_label = max_num
            while pick.contains(dst_label):
                dst_label -= 1
                if dst_label < min_num:
                    dst_label = max_num

            m[dst_label].insert_right(pick)
            current_label = m[current_label].next.val

        result = m[1].next.val * m[1].next.next.val
        print(result)
        assert(result == 693659135400)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
