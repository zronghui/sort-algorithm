#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors


def swap(a, i, j):
    print(f'swap {a[i]} and {a[j]}')
    a[i], a[j] = a[j], a[i]
    print(a)


def sortAndAssert(f):
    a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    result = f(a)
    a = result if result else a
    print(a)
    right = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
    print(right)
    for i in range(len(a)):
        assert a[i] == right[i], f'{a[i]} {right[i]}'
