#!/usr/bin/python
#coding=utf-8

"""
生产者-消费者模式

生产者 每生产一个对象，休息1秒
"""

import threading, time, random
from queue import Queue
from collections import namedtuple

# 馒头对象
Bread = namedtuple('Bread', ['name'])

class Basket(object):

    def __init__(self, size=5):
        self._size = size        # 容器的大小
        self._basket = Queue()   # 容器
        self._counter = 1

    def go_sleep(self):
        sleep_time = random.randint(1, 5)

        print('*********休息 %d--活跃流水线：%d' % (sleep_time, threading.active_count()))
        time.sleep(sleep_time)

    @property
    def is_full(self):
        """ 是否已经满了 """
        return self._basket.qsize() >= self._size

    @property
    def is_empty(self):
        """ 是否为空 """
        return self._basket.qsize()  == 0

    def push(self):
        """ 添加馒头 """
        # 线程用户
        thread_name = threading.current_thread().name
        name = "Bread_%03d" % self._counter
        self._counter += 1
        bread = Bread(name=name)
        self._basket.put(bread)
        print(">> %s 生产馒头：%s , 共有 %03d 馒头" % (thread_name, name, self._basket.qsize()))

    def pop(self):
        """ 消费馒头 """
        # 线程用户
        thread_name = threading.current_thread().name
        if not self.is_empty:
            bread = self._basket.get()
            print("<< %s 消费馒头：%s , 共有 %03d 馒头" % (thread_name, bread.name, self._basket.qsize()))
        else:
            print("------------------没有馒头了------------------")



class Producer(threading.Thread):
    """ 生产者 """

    def __init__(self, basket, condition, name=None):
        super(Producer, self).__init__(name=name)
        self._basket = basket
        self._condition = condition

    def run(self):
        """ 生产者用于生产馒头 """
        while True:
            try:
                # 加锁
                self._condition.acquire()
                if self._basket.is_full:
                    print("------------满了--------------")
                    self._condition.notify_all()
                    self._condition.wait()
                else:
                    # 开始生产
                    self._basket.push()
                    self._basket.go_sleep()
            finally:
                # 释放锁
                self._condition.release()


class Consumer(threading.Thread):
    """ 消费者 """
    def __init__(self, basket, condition, name=None):
        super(Consumer, self).__init__(name=name)
        self._basket = basket
        self._condition = condition

    def run(self):
        """ 消费者用于消费馒头 """
        while True:
            try:
                # 加锁
                self._condition.acquire()
                if self._basket.is_empty:
                    print("------------空了--------------")
                    self._condition.notify_all()
                    self._condition.wait()
                else:
                    # 开始消费
                    self._basket.pop()
                    self._basket.go_sleep()
            finally:
                # 释放锁
                self._condition.release()

def test():
    basket = Basket(5)
    condition = threading.Condition()
    for i in range(5):
        name = 'P_%d' % i
        print('开启生产线>>>%s' % name)
        p = Producer(basket, condition, name=name)
        p.start()

    print('--------休息一下，准备开始消费')
    basket.go_sleep()
    print('---------开始消费----------')
    for i in range(4):
        name = 'C_%d' % i
        print('开启消费线>>>%s' % name)
        c = Consumer(basket, condition, name=name)
        c.start()

if __name__ == '__main__':
    test()
