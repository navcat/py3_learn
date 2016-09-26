#!/usr/bin/python
#coding=utf-8

import time
import os, random
from multiprocessing import Process, Pool


def run_proc(name):
    """ 子进程要执行的代码 """
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(5)  # 休息5秒钟
    print("time is sleeping done.")

def use_process():
    """ 进程 """
    print("Parent process : %d" % os.getpid())
    p = Process(target=run_proc, args=["test"])
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def use_pool():
    """ 使用进程池 """
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

if __name__ == '__main__':
    # use_process()
    use_pool()
