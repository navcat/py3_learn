#!/usr/bin/python
#coding=utf-8

import threading, time


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def test_loop():
	print('thread %s is running...' % threading.current_thread().name)
	t = threading.Thread(target=loop, name='LoopThread')
	print('t.name:', t.name)
	t.start()
	t.join()
	print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
	test_loop()