#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
from common import swap, sortAndAssert

'''
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''


def insertionSort(a):
    n = len(a)
    if n < 2:
        return a
    for i in range(1, n):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t


def insertionSort1(a):
    # 低效、错误的代码
    n = len(a)
    if n < 2:
        return a
    for i in range(1, n):
        for j in reversed(range(i)):
            if a[j] <= a[i]:
                break
            swap(a, i, j)
            i = j  # 记得更新 i，为的是把 i 插入正确的位置


def insertionSort2(a):
    n = len(a)
    if n < 2:
        return a
    for i in range(1, n):
        t = a[i]  # 暂存需要插入的值
        # 可能插在首位, 所以加上 -1
        for j in reversed(range(-1, i)):
            if j == -1 or a[j] <= t:
                a[j + 1] = t
                break
            a[j + 1] = a[j]


if __name__ == '__main__':
    sortAndAssert(insertionSort)
    sortAndAssert(insertionSort1)
    sortAndAssert(insertionSort2)
