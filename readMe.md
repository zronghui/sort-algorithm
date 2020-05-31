[Introduction - 十大经典排序算法](https://sort.hust.cc/)

[冒泡排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/1.bubbleSort.md)

```
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
```

```python
def bubbleSort(a):
    n = len(a)
    if n < 2:
        return a
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                swap(a, i, j)
```

[选择排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/2.selectionSort.md)

```
1. 首先在未排序序列中找到最小元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
```

```python
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
```

[插入排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/3.insertionSort.md)

```
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
```

```python
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
```

[希尔排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/4.shellSort.md)

```
增量的插入排序
起始 gap = int(n/3)
一次 插入排序， gap = int(gap/3)
```

```python
def shellSort(a):
    n = len(a)
    if n < 2:
        return a
    gap = int(n / 3)
    while gap > 0:
        for i in range(gap, n):
            t = a[i]
            j = i - gap
            while j >= 0 and a[j] > t:
                a[j + gap] = a[j]
                j -= gap
            a[j+gap] = t
        gap = int(gap / 3)
```

[归并排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/5.mergeSort.md)

```
归并排序的实现由两种方法：
自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
自下而上的迭代；

归并排序：归并 2 个已经排好序的子序列
```

```python
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
```



[快速排序](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/6.quickSort.md)

```python
def partition(a, left, right):
    # pivot = a[left]
    # 数组 a 从索引 left+1 到 right 中
    # 把比 pivot 大的都放右边，比 pivot 小的都放左边
    # 最后返回 pivot 的索引

    # 可以记录比 pivot 小的数的最大索引，然后和 pivot 交换
    # 举例：[3, 2, 5, 1, 6]--> [3, 2, 1, 5, 6] --> [1, 2, 3, 5, 6]
    # 首先分成 2 1 和 5 6，比 pivot 小的最大位置是 1 ，和 3 交换即可，最后返回 3 的索引
    pivot = left
    # i 用来遍历，index-1 标记比 pivot 小的数的最大位置
    i = index = left + 1
    while i <= right:
        if a[i] < a[pivot]:
            swap(a, i, index)
            index += 1
        i += 1
    swap(a, index - 1, pivot)
    return index - 1


def quickSort(a, left=None, right=None):
    n = len(a)
    left = 0 if left is None else left
    right = n - 1 if right is None else right
    if n < 2 or right - left < 1:
        return
    p = partition(a, left, right)
    quickSort(a, left, p - 1)
    quickSort(a, p + 1, right)

```

