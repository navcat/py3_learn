#!/usr/bin/python
#coding=utf-8

"""
使用协程实现的文件查找器

"""

import os
import fnmatch
import gzip
import bz2
import sys
from functools import wraps

def coroutine(func):
    """ 协程装饰器，调用一次next，进入等待 """
    @wraps(func)
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper

@coroutine
def find_files(target):
    print('Starting to find..')
    while True:
        topdir, pattern = (yield)
        print('Recieve data: %s, %s' % (topdir, pattern))
        for path, dirname, filelist in os.walk(topdir):
            for name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    target.send(os.path.join(path, name))


@coroutine
def opener(target):
    print('Prepare to opener')
    while True:
        name = (yield)
        if name.endswith('.gz'):
            f = gzip.oepn(name)
        elif name.endswith('.bz2'):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        target.send(f)

@coroutine
def cat(target):
    print('Prepare to cat file')
    while True:
        f = (yield)
        for line in f:
            target.send(line)

@coroutine
def grep(pattern, target):
    print('Prepare to grep data')
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    print('Prepare to printing')
    while True:
        line = (yield)
        sys.stdout.write(line)


def test_main():
    """ 测试类 """
    finder = find_files(opener(cat(grep('python', printer()))))
    # 发送值
    finder.send(('www', 'access-log'))

if __name__ == '__main__':
    test_main()