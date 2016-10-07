#!/usr/bin/python
#coding=utf-8

"""
用线程实现
生产者-消费者模式

生产者 每生产一个馒头，休息1秒
"""
import time, threading, random
from collections import namedtuple

# 馒头对象
Bread = namedtuple('Bread', ['name'])

# 篮子，用来装馒头
basket = []
basket_size = 20

counter = 0


def producer():
	""" 生产馒头 """
	global counter
	name = threading.current_thread().name
	while True:
		if len(basket) >= basket_size:
			print('$$$$$$仓库已经装满了，%s 已经退出$$$$$$$$' % name)
			break
			# time.sleep(5)
		else:
			counter += 1
			# 馒头名称
			bread_name = 'bread%d' % counter
			bread = Bread(name=bread_name)
			# 休息时间
			sleep_time = random.randint(1,5)
			basket.append(bread)
			print('>>%s 生产馒头: %s ;总共 %d 个馒头;休息 %d 秒' % (name, bread_name, len(basket), sleep_time))
			time.sleep(sleep_time)


def consumer():
	""" 消费者 """
	name = threading.current_thread().name
	while True:
		if len(basket) > 0:
			bread = basket.pop()
			# 休息时间
			sleep_time = random.randint(1,5)
			print('<<<<<<<<<< %s 消费馒头: %s ;总共 %d 个馒头;休息 %d 秒' % (name, bread.name, len(basket), sleep_time))
			time.sleep(sleep_time)
		else:
			print('###########馒头已经消费完毕，%s 已经退出###########' % name)
			break


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
	factory.produce()
	factory.consume()
