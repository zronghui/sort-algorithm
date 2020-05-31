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
    pass


def quickSort(a, left=None, right=None):
    pass


if __name__ == '__main__':
    sortAndAssert(quickSort)
