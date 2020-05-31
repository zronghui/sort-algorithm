#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors

from common import swap, sortAndAssert

'''
1. 首先在未排序序列中找到最小元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
'''


# range(10, 0, -1)   10, 9, ..., 0

def selectionSort(a):
    n = len(a)
    if n < 2:
        return a
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            if a[j] < a[mi]:
                mi = j
        swap(a, i, mi)


if __name__ == '__main__':
    sortAndAssert(selectionSort)
