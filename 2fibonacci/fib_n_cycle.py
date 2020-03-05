# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 7:31 下午
# @Author  : lihm
# @File    : fib_n_cycle.py


from time import time


# 空间 O(n)

def count_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fn = 0
        fn_1 = 1
        for i in range(n):
            tmp = fn_1
            fn_1 += fn
            fn = tmp

        return fn_1



if __name__ == '__main__':
    count_n = 1000
    start = time()
    k=count_fibonacci(count_n)
    print(k)
    end = time()
    count_time = end - start
    print(count_time)