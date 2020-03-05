# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 7:40 下午
# @Author  : lihm
# @File    : fib_logn_recursive.py

from time import time

# 矩阵
# 递归循环
# 空间复杂度 O(logn)
# 时间复杂度 O(logn)

# return fn+1 fnf
def fibonacci(n):
    # odd
    if n > 0:
        m = int(n / 2)
        fm_1, fm = fibonacci(m)

        if n % 2:
            fn_1 = fm_1 * (fm_1 + 2*fm)
            fn = fm_1 * fm_1 + fm * fm
        # even
        else:
            fn_1 = fm_1 * fm_1 + fm * fm
            fn = fm * (2 * fm_1 - fm)

        return fn_1, fn
    else:
        return 1, 0


def count_fibonacci(n):
    return fibonacci(n)[1]

if __name__ == '__main__':
    count_n = 5
    start = time()
    print(count_fibonacci(count_n))
    end = time()
    count_time = end - start
    print(count_time)