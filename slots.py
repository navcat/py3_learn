#!usr/bin/python
#coding=utf-8

"""
1, __slots__定义的属性仅对当前类实例起作用
2, 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

"""

class People(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_msg(self):
        print('name: %s, age:%s' % (self.name, self.age))


class Student(People):

    __slots__ = ('score')

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_msg(self):
        print('name: %s, age:%s, score: %s' % (self.name, self.age, self.score))


def bind_func():
    print('this is bind function')

def main():

    # 对象的调用
    people = People('张珊', 34)
    people.print_msg()

    student = Student('李四', 21, 90)
    student.print_msg()


    # 可以更改允许的属性值
    people.age = 99
    print(people.age)


    # 无法绑定方法
    people.bind_func = bind_func
    people.bind_func()

    # 无法更改不允许的值
    people.score = 99
    print(people.score)

    student.status = 1
    print(student.status)


if __name__ == '__main__':
    main()