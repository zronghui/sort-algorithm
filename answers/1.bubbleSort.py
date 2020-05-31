#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 5:06 下午
# @Author  : zhangronghui
# @File    : 1.bubblesort.py
# @Software: PyCharm
import pretty_errors

from common import swap, sortAndAssert

'''
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''


def bubbleSort(a):
    n = len(a)
    if n < 2:
        return a
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                swap(a, i, j)


if __name__ == '__main__':
    sortAndAssert(bubbleSort)
