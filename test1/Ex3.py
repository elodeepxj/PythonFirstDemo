# -*- coding:utf-8 -*-

print "----------切片----------"
L=range(100)
print L[:5]#取出前5个元素
print L[1:5]#取出第二个到第五个元素
print L[-3:]#取出倒数3个元素
print L[:10:2]#取出前10个元素，每两个取一个
print L[::5]#取出所有元素，每五个取一个
print L[:]#取出所有元素

print "----------迭代----------"
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key,
print
for value in d.itervalues():
    print value,
print
for x,key in enumerate(d):#enumerate可以获取下标
    print x,key,
print
print "----------列表生成式----------"
print range(0,10)#生成从0开始到10结束的集合
print range(0,10,2)#生成从0开始到10结束,每2个生成一个元素的集合
print [x*x for x in range(1,5) if x%2 ==0]#生成元素为偶数的平方集合
print [m+n for m in 'ABC' for n in 'xyz']#双层循环
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s,str) else s for s in L ]

print "----------生成器----------"
g = (x*x for x in range(1,10))#g就是一个生成器，和集合的区别，集合是【】，生成器是（）
for i in g:
    print i,







