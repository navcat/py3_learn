#!usr/bin/python
#coding=utf-8

"""
python 面向对象

__开头的是私有变量，只能内部访问
"""

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))


def main():
	"""
	>> 张三: 88
	>> 88
	>> 张三
	>> Traceback (most recent call last):
	  File "oop.py", line 26, in <module>
	    main()
	  File "oop.py", line 23, in main
	    print(student.__name)
	AttributeError: 'Student' object has no attribute '__name'
	"""
	student = Student("张三", 88)
	student.print_score()
	print(student.score)

	# 这里是可以的，但是强烈建议你不要这么做，因为不同版本的Python解释器可能会把__name改成不同的变量名。
	print(student._Student__name)
	print(student.__name)   # 这里是没法访问的

if __name__ == '__main__':
	main()