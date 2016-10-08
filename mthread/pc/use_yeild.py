#!/usr/bin/python
#coding=utf-8

"""
生产者-消费者模式
"""

from collections import namedtuple
from queue import Queue

# 馒头对象
Bread = namedtuple('Bread', ['name'])

counter = 1
# 篮子，用来装馒头
basket = Queue()
basket_size = 5

def consumer():
	""" 消费者 """
	bread = None
	while True:
		bread = yield bread
		if bread:
			print('消费 %s' % bread.name)
		else:
			print('-------none-------')
			break


def producer(c):
	""" 生产者 """
	global counter
	c.send(None)
	while True:
		if basket.qsize() > basket_size:
			print('--------full---------')
			break
		else:
			name = 'Bread_%03d' % counter
			counter += 1
			bread = Bread(name=name)
			basket.put(bread)
			print('生产 %s; 共 %d 个馒头.' % (name, basket.qsize()))
			c.send(bread)
	c.close()



def main():
	""" 测试 """
	c = consumer()
	producer(c)

if __name__ == '__main__':
	main()