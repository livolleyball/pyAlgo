# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 9:50 下午
# @Author  : lihm
# @File    : sort.py


import random


def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quicksort(left) + [base] + quicksort(right)


def bouble_sourt(seq):
    # 冒泡排序（顺序形式），从左向右，两两比较，如果左边元素大于右边，就交换两个元素的位置。
    # 其中，每一轮排序，序列中最大的元素浮动到最右面。也就是说，每一轮排序，至少确保有一个元素在正确的位置。
    # 这样接下来的循环，就不需要考虑已经排好序的元素了，每次内层循环次数都会减一。
    # 其中，如果有一轮循环之后，次序并没有交换，这时我们就可以停止循环，得到我们想要的有序序列了。
    seq = seq[:]

    n = len(seq) - 1
    i = j = 0
    flag = 1
    # 遍历所有数组元素
    while i < n:
        j = 0
        # Last i elements are already in place
        while j < n - i - 1:
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                flag = 0
            j += 1
        if flag:
            break
        i += 1

    return seq


def find_min_index(seq):
    min_elem = seq[0] 
    count = 0
    min_leem_index = count
    for elem in seq[1:]:
        count += 1
        if elem < min_elem:
            elem, min_elem = min_elem, elem
            min_leem_index = count
    return min_leem_index


def select_sort(seq):
    # 选择排序
    seq = seq[:]
    length = len(seq)
    for i in range(length):
        index = find_min_index(seq[i:])
        seq[index + i], seq[i] = seq[i], seq[index + i]
    return seq


if __name__ == '__main__':
    seq = [9, 1, 2, 5, 4, 3, 2, 1, 4]
    random.shuffle(seq)
    print(quicksort(seq))
    print(bouble_sourt(seq))
    print(select_sort(seq))
