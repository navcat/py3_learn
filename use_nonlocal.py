#!/usr/bin/python
#coding=utf-8

"""
nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

仅支持py3

"""

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
    
def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


if __name__ == '__main__':
  make_counter_test()