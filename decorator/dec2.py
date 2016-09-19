#!usr/bin/python
#coding=utf-8

"""
python 装饰器

传递参数
"""
from functools import wraps

def log(text=None):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("---logstart----")
            print('%s %s():' % (text, func.__name__))
            rest = func(*args, **kwargs)
            print("---logend----")
            return rest
        return wrapper
    return decorator

@log("execute")
def now():
    print('2016-9-19 19:09:51')


if __name__ == '__main__':
    now()
    # 在不添加wraps时now.__name__ = wrapper
    print(now.__name__)
