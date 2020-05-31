#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
from common import swap, sortAndAssert


def mergeSort(a):
    n = len(a)
    if n < 2:
        return a
    mid = int(n / 2)
    left, right = a[:mid], a[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    res = []
    while left and right:
        a = left[0]
        b = right[0]
        if a <= b:
            res.append(a)
            left.pop(0)
        else:
            res.append(b)
            right.pop(0)
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


if __name__ == '__main__':
    sortAndAssert(mergeSort)
