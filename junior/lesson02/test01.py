# coding: utf-8
import string
#简单类型
print type(1234)
print type(12.123)
print type(123.)
print type('abc')
print type("abc")
#容器
print type([1,23,4])
print type((12,2,3))
print type(set([1,2,2,3]))
print type({'a':1,'b':2})
#函数
def func(a,b,c):
	return a + b + c
	pass
afunc = func
print type(func)
print type(afunc)

#模块
print type(string)

#类

class MyClass(object):
	"""docstring for MyClass"""
	def __init__(self, arg):
		super(MyClass, self).__init__()
		self.arg = arg
	pass

aclass = MyClass(123)
#定义的类属于type类型
print type(MyClass)
#实例化的类属于对应的类的类型
print type(aclass)