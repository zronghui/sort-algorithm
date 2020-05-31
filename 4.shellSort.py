#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
from common import swap, sortAndAssert

'''
1. 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


一个更好理解的希尔排序实现：
将数组列在一个表中并对列排序（用插入排序）。
重复这过程，不过每次用更长的列来进行。
最后整个表就只有一列
将数组转换至表是为了更好地理解这算法，算法本身仅仅对原数组进行排序
'''


def shellSort(a):
    pass


if __name__ == '__main__':
    sortAndAssert(shellSort)
