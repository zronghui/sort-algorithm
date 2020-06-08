#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
from common import swap, sortAndAssert


def partition(a, left, right):
    # pivot = a[left]
    # 数组 a 从索引 left+1 到 right 中
    # 把比 pivot 大的都放右边，比 pivot 小的都放左边
    # 最后返回 pivot 的索引

    # 可以记录比 pivot 小的数的最大索引，然后和 pivot 交换
    # 举例：[3, 2, 5, 1, 6]--> [3, 2, 1, 5, 6] --> [1, 2, 3, 5, 6]
    # 首先分成 2 1 和 5 6，比 pivot 小的最大位置是 1 ，和 3 交换即可，最后返回 3 的索引
    # p2 用来遍历，p1-1 标记比 pivot 小的数的最大位置
    pivot = a[left]
    p1 = p2 = left + 1
    while p2 <= right:
        if a[p2] < pivot:
            swap(a, p1, p2)
            p1 += 1
        p2 += 1
    swap(a, p1 - 1, left)
    return p1 - 1


def quickSort(a, left=None, right=None):
    left = 0 if left is None else left
    right = len(a) - 1 if right is None else right
    if right - left < 1:
        return a
    pivot = partition(a, left, right)
    quickSort(a, left, pivot - 1)
    quickSort(a, pivot + 1, right)


if __name__ == '__main__':
    sortAndAssert(quickSort)
