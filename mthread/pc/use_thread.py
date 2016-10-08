#!/usr/bin/python
#coding=utf-8

"""
用线程实现
生产者-消费者模式

生产者 总共5条流水线，每生产一个馒头，随机休息1-5秒
消费者 总共4条流水线，每消费一个馒头，随机休息1-5秒
"""
import time, threading, random
from collections import namedtuple, deque

# 馒头对象
Bread = namedtuple('Bread', ['name'])

# 篮子，用来装馒头
basket = deque()
basket_size = 5

counter = 0
# lock = threading.Lock()
condition = threading.Condition()


def producer():
    """ 生产馒头 """
    global counter
    name = threading.current_thread().name
    while True:
        try:
            condition.acquire()
            if counter > 10000:
                print('终点-------')
                break
            if len(list(basket)) >= basket_size:
                print('------------仓库已经装满了，%s 现在暂停------------' % name)
                condition.notify()
                condition.wait()
            else:
                counter += 1
                # 馒头名称
                bread_name = 'bread_%03d' % counter
                bread = Bread(name=bread_name)
                # 休息时间
                sleep_time = random.randint(1,5)
                basket.append(bread)
                print('>>%s 生产馒头: %s ;总共 %03d 个馒头;休息 %d 秒' % (name, bread_name, len(basket), sleep_time))
                time.sleep(sleep_time)
        finally:
            condition.release()


def consumer():
    """ 消费者 """
    name = threading.current_thread().name
    while True:
        try:
            condition.acquire()
            if len(list(basket)) > 0:
                bread = basket.popleft()
                # 休息时间
                sleep_time = random.randint(1,5)
                print('<<%s 消费馒头: %s ;总共 %03d 个馒头;休息 %d 秒' % (name, bread.name, len(basket), sleep_time))
                time.sleep(sleep_time)
            else:
                print('------------馒头已经消费完毕，%s 已经退出--------------' % name)
                condition.notify()
                condition.wait()
        finally:
            condition.release()


class Factory(object):
    """ 工厂，执行生产和消费 """

    def produce(self):
        """ 启用5个线程开始生产 """
        for i in range(5):
            name = 'P_%d' % i
            print('开启生产线>>>%s' % name)
            t = threading.Thread(target=producer, name=name)
            t.start()

    def consume(self):
        """ 启用4个线程开始消费 """
        for i in range(4):
            name = 'C_%d' % i
            print('开启消费线>>>%s' % name)
            t = threading.Thread(target=consumer, name=name)
            t.start()

if __name__ == '__main__':
    factory = Factory()
    print('------------开始生产------------------------')
    factory.produce()
    # print('------------5s后开始消费------------------------')
    # time.sleep(5)
    print('------------开始消费------------------------')
    factory.consume()
