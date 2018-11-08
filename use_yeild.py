#!/usr/bin/python
#coding=utf-8

"""

当调用next()时，生成器函数将不断执行语句，直到遇到yield为止。
yield语句在函数执行停止的地方产生一个结果，直到再次调用next()。
然后继续执行yield之后的语句。

当yield出现在赋值运算符右侧时，如（n = (yield)）,
    这种函数则称为协程，它的执行是为了响应发给它的值。
"""

from functools import wraps

def count_down(n):
    """ yield语句的使用 """
    print('Counting down from %d' % n)
    while n > 0:
        yield n
        n -= 1
    return

def test_count_down():
    """ 测试yield 语句 """
    cd = count_down(10)
    print(next(cd))
    print(next(cd))
    print(next(cd))
    print(cd.__next__())    # py3.x 中使用
    # print(cd.next())      # py2.x中使用
    print(dir(cd))
    cd.close()     # 关闭生成器

    # 可以直接用for循环调用
    for n in count_down(10):
        print(n)


def receiver():
    """ yield当做赋值语句来使用，协程 """
    print('Ready to receive data.')
    while True:
        n = (yield)
        print('Got a data : %s' % n)


def test_receiver():
    """ 协程测试 """
    rec = receiver()
    # 首先需要调用一次，进入到函数中，遇到第一个yield，函数会停止等待
    # 此处建议使用装饰器，见下例子
    next(rec)
    rec.send(1)
    rec.send(2)
    rec.send('Hello')
    rec.send([1,2,3])
    # 关闭协程
    rec.close()


def coroutine(func):
    """ 协程装饰器，调用一次next，进入等待 """
    @wraps(func)
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


@coroutine
def receiver2():
    """ yield当做赋值语句来使用，协程 """
    print('Ready to receive data.')
    while True:
        n = (yield)
        print('Got a data : %s' % n)

def test_receiver2():
    """ 协程测试 """
    rec = receiver2()
    rec.send(1)
    rec.send(2)
    rec.send('Hello')
    rec.send([1,2,3])
    rec.close()


@coroutine
def receiver_with_param(spliter):
    """ yield with params """
    print('Ready to receive data.')
    result = None
    while True:
        n = (yield result)
        result = n.split(spliter)
        print('Got a data : %s' % n)

def test_receiver_with_param():
    """ 协程测试 """
    rec = receiver_with_param(',')
    data = rec.send("1,23,4")
    print('The return data : %s' % data)
    print(rec.send('Hello, world'))
    rec.close()

if __name__ == '__main__':
    # 测试yield
    # test_count_down()
    # 协程测试
    test_receiver()
    # test_receiver2()
    # test_receiver_with_param()