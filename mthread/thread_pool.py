#!/usr/bin/python
#coding=utf-8

import threading, time
from multiprocessing.dummy import Pool as ThreadPool

"""
线程池
Python中线程multiprocessing模块与进程使用的同一模块。
使用方法也基本相同，唯一不同的是，from multiprocessing import Pool这样导入的Pool表示的是进程池；
from multiprocessing.dummy import Pool这样导入的Pool表示的是线程池。这样就可以实现线程里面的并发了。
"""

def run(n):
    time.sleep(1)
    print(n)

def main():
    n_list = [1, 2, 3, 4, 5, 6, 7]
    # 创建容量为10的线程池
    pool = ThreadPool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()