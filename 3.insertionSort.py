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
    pass


if __name__ == '__main__':
    sortAndAssert(insertionSort)
