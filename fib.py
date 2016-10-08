#!/usr/bin/python
#coding=utf-8

"""
斐波拉契数列

1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

def fib(num):
    """
    n: 第几个数
    l: 存放数列
    """
    a, b, n, l = 0, 1, 1, []
    while n <= num:
        l.append(b)
        a, b = b, a + b
        n += 1
    return l


def fib_1(num):
    """ 使用递归 """
    if num <= 2:
        return 1
    return fib_1(num-1) + fib_1(num - 2)

def fib_2(num):
    """ 使用递归缩写 """
    return 1 if num <= 2 else fib_2(num-1) + fib_2(num - 2)

def fib_3(num):
    a, b, n = 0, 1, 1
    while n <= num:
        yield b
        a, b = b, a + b
        n += 1


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        # 实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a

    def __str__(self):
        return 'Fib class'

    def __repr__(self):
        """
        区别是__str__()返回用户看到的字符串，
        而__repr__()返回程序开发者看到的字符串，
        也就是说，__repr__()是为调试服务的
        """
        return self.__str__()

    def __getitem__(self, n):
        """
        获取第N个数 
        可以直接用Fib[5]来调用
        """

        # slice表示切片
        if isinstance(n, slice):
            start = 0 if n.start is None else n.start
            stop = 100 if n.stop is None else n.stop
            step = n.step
            # TODO step 负数
            a, b = 0, 1
            l = []
            for i in range(stop):
                a, b = b, a + b
                if i >= start:
                    l.append(a)
            return l
        else:
            def _fib(n):
                return 1 if n <= 2 else _fib(n-1) + _fib(n - 2)
            return _fib(n)


    def __getattr__(self, attr):
        if attr == 'x':
            return 'X data'
        if attr == 'y':
            return lambda: 45
        else:
            return 'No data'

    def __call__(self):
        """ 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用 """
        print('This is from call')
        return 'Call done.'


if __name__ == '__main__':
    # print('-------------')
    # print(fib(5))
    # print('-------------')
    # print(fib_1(5))
    # print('-------------')
    # print(fib_2(5))
    # print('-------------')
    # res = fib_3(5)
    # print(next(res))
    # print(next(res))
    # print(next(res))
    # print(next(res))
    # print(next(res))
    print('-------------')

    f = Fib()
    # # 打印__str__返回的值
    # print(f)
    # # 根据索引取数据
    # print(f[6])
    # 可以使用切片
    print(f[6: ])
    # 可以使用循环
    # for i in f:
    #     print(i)
    # 获取不存在的属性
    print(f.x)
    print(f.y())
    print(f.z)
    # 进行实例调用
    print(callable(f))
    print(f())
