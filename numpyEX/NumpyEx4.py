# -*- coding:utf-8 -*-
#文件读写
import numpy as np
print "-----------写入文件----------"
i = np.eye(2)# 创建单位矩阵，对角线上的元素为1，其余为0
print i
np.savetxt("f:/eye.txt",i)

print "---------从CSV文件读取数据------------"
c,v = np.loadtxt("f:/kaggle/titanic/train.csv",delimiter=',',usecols=(0,1),unpack=True,skiprows=1)#数据第一行是String类型的title，skiprows=1跳过第一行
#usecols:使用第0第1列,unpack:是否分开存储
print c,v

print "计算平均值"
print np.average(c)#平均值
print np.average(c,weights=v)# 加权平均值
print np.mean(c)#平均值
print np.max(c)#最大值
print np.min(c)#最小值
print np.ptp(c)#最大值和最小值的差值
