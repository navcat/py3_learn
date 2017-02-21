#!/usr/bin/python
#coding=utf-8

from collections import OrderedDict

class FiFoDict(OrderedDict):
	'''
	定义一个先进先出的dict
	'''
	def __init__(self, size):
		super(FiFoDict, self).__init__()
		self._size = size

	def __setitem__(self, key, value):
		if key not in self and len(self) >= self._size:
			item = self.popitem(last=False)
			print("delete:", item)
		super(FiFoDict, self).__setitem__(key, value)

if __name__ == '__main__':
	d = FiFoDict(3)
	d["a"] = 1
	print("##d1", d)
	d["b"] = 1
	print("##d2", d)
	d["c"] = 1
	print("##d3", d)
	d["d"] = 1
	print("##d4", d)
	d["c"] = 2
	print("##d5", d)