# coding: utf-8
#字符串相关处理
import string

#去除空格
s = ' abcd efg '
print('lll' + s.strip() + 'lll')
print('lll' + s.lstrip() + 'lll')
print('lll' + s.rstrip() + 'lll')

#连接字符串
a = 'abc'
b = 'DEF'
print (a + b)

#大小写
print(a.upper())
print(b.lower())
print(a.capitalize())
print(b.capitalize())

#位置比较
str1 = 'abcd'
str2 = 'abcdef'
print str2.index(str1)

if not '' :
	print 'Empty'

#分割和连接
s = 'abc,def,ghi'
print s.split(',')
s = """abc
def
"""
print s.splitlines()
s = ['abc', '123']
print ','.join(s)
print '123'.isalnum()
print '123w'.isalnum()
print '123c'.isdigit()
print 'abc'.isalpha()

#可变参数 
#tuple
def func(name, *numbers):
	print numbers
	pass
func('tom', 1, 2, 3, 'abc')
#ditc
def funcDict(name, **kvs):
	print kvs
	pass
funcDict('tom', china = 'beijing', uk = 'London')

#递归 
#求和
def my_sum(i):
	if i < 0:
		raise ValueError
	elif i <= 1:
		return i
	else:
		return i + my_sum(i - 1)
	pass
print my_sum(100)
#求斐波那契数列
def my_feibonaqie(i):
	if i < 0:
		raise ValueError
	elif i <= 2:
		return 1
	else:
		return my_feibonaqie(i - 1) + my_feibonaqie(i - 2)
	pass
print my_feibonaqie(5)
#汉诺塔问题
def hanoi(n, source, target, hepler):
	if n <= 0:
		raise ValueError
		pass
	elif n == 1:
		print source + ' -> ' + target
	elif n >= 2:
		hanoi(n - 1, source, hepler, target)
		print source + ' -> ' + target
		hanoi(n - 1, hepler, target, source)
	pass

hanoi(3, 'A', 'B', 'C')