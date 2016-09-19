#!usr/bin/python
#coding=utf-8

"""
python 装饰器

不需要传递参数的部分
"""

from functools import wraps

def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("---logstart----")
        rest = func(*args, **kwargs)
        print("---logend----")
        return rest
    return wrapper

@log
def now():
    print('2016-9-19 19:09:51')


if __name__ == '__main__':
    now()
    # 在不添加wraps时now.__name__ = wrapper
    print(now.__name__)
