#!/usr/bin/python
#coding=utf-8

import threading, time

"""
使用join的一个举例
"""

def join():
    print('In thread join')
    time.sleep(1)
    print('Out thread join')

def context(thread_join):
    print('In context')
    # 阻止线程直到thread_join执行完成
    thread_join.start()
    thread_join.join()
    # 执行完成，释放
    print('Out context')

def main():
    """
    >> In context
    >> In thread join
    >> Out thread join
    >> Out context
    """
    t_join = threading.Thread(target=join)
    t_context = threading.Thread(target=context, args=(t_join, ))
    t_context.start()


if __name__ == '__main__':
    main()
