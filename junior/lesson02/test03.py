# coding: utf-8
#字符串按单词反转
s = 'I love China!  '
alist = s.split(' ')
alist.reverse()
print ' '.join(alist)

#打印10000以内的所有素数

for i in xrange(2, 10000):
	flag = True
	for j in xrange(2,int(i ** 0.5 + 1)):
		if i % j == 0:
			flag = False
		pass
	if flag:
		print i
	pass