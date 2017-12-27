# -*- coding:utf-8 -*-
#数组纬度改变
import numpy as np

a = np.arange(5)
print a
print a.shape
b = np.array([np.arange(3),np.arange(3)])
print b
print b.shape
c=np.array([a,a])
print c

d = np.arange(7,dtype='d')
print d

f = np.arange(24).reshape(2,3,4)
print f
print f[:,:,1]
print f[:,::-1,-1]
print "------------------------"
print np.ravel(f)# 数组展平，不保存结果
print f.flatten()# 数组展平，保存结果
print f.reshape(6,4)#数据纬度修改
print np.transpose(f)#矩阵转置
f.resize(2,12)#数据纬度修改
print f