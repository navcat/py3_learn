#!usr/bin/python
#coding=utf-8

"""
单例模式的实现

方式一：使用__new__
方式二： 共享属性
方式三： 使用装饰器
"""

class Singleton(object):
    """ 使用__new__来实现单例模式 """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyTest(Singleton):
    pass

class MyTestExtend(MyTest):
    pass

def test_01():
    """测试1"""
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()
    m1 = MyTest()
    m2 = MyTest()
    me1 = MyTestExtend()
    me2 = MyTestExtend()
    print(id(s1))
    print(id(s2))
    print(id(s3))
    print(id(m1))
    print(id(m2))
    print(id(me1))
    print(id(me1))
    print(isinstance(m1, Singleton))
    print(isinstance(m1, MyTest))
    print(isinstance(me1, Singleton))
    print(isinstance(me1, MyTestExtend))


class Borg(object):
    """ 使用共享属性来实现单例模式
    所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)  
    同一个类的所有实例天然拥有相同的行为(方法),  
    只需要保证同一个类的所有实例具有相同的状态(属性)即可  
    所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)  
    """
    _state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj

class MyBorg(Borg):
    pass

def test_02():
    b1 = Borg()
    b2 = MyBorg()
    print(id(b1))
    print(id(b2))
    print(b1 == b2)
    print(b1.__dict__ == b2.__dict__)


def singleton(cls, *args, **kwargs):
    """ 使用装饰器实现单例模式 """
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance['cls'] = cls(*args, **kwargs)
        return instance['cls']
    return get_instance

@singleton
class MySingle(object):
    pass

# class MySingle2(MySingle):
#     pass

def test_03():
    print(id(MySingle()))
    print(id(MySingle()))
    print(id(MySingle()))
    # print(id(MySingle2()))
    # print(id(MySingle2()))


if __name__ == '__main__':
    test_01()
    print('-------2------')
    test_02()
    print('-------3------')
    test_03()
