# -*- coding:utf-8 -*-
#数组的分割
import numpy as np

# x = np.arange(3)
# y = x+3
# z = y+3
# a = np.array([x,y,z])
a = np.arange(9).reshape(3,3)
print a
print "-----------水平分割-----------"
ha = np.hsplit(a,3)#水平分割，对数组a进行水平分割，分割成3份
print ha

sha = np.split(a,3,axis=1) #效果等同水平分割
print sha

print "-----------垂直分割-----------"
va = np.vsplit(a,3)# 垂直分割
print va

sva = np.split(a,3,axis=0) #效果等同垂直分割 axis=0或者不写
print sva

print "-----------深度分割-----------"
b = np.arange(27).reshape(3,3,3)
print b

db = np.dsplit(b,3)
print db
sdb = np.split(b,3,axis=2) #效果等同深度分割 axis=2
print sdb



x = np.arange(0,8).reshape(4,2)
print x
print x.T# 效果等同transpose函数
print x.tolist()# 把数组转换成集合