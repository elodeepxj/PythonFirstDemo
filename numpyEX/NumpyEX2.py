# -*- coding:utf-8 -*-
#数组的组合
import numpy as np

a = np.arange(6).reshape(2,3)
b = a*2
print a
# [[0 1 2]
#  [3 4 5]]
print b
# [[ 0  2  4]
#  [ 6  8 10]]
print "-----------水平组合-----------"
hc = np.hstack((a,b))# 水平组合
hd = np.hstack((b,a))
print hc
# [[ 0  1  2  0  2  4]
#  [ 3  4  5  6  8 10]]
print hd
# [[ 0  2  4  0  1  2]
#  [ 6  8 10  3  4  5]]

hc1 = np.concatenate((a, b), axis=1)# concatenate也能实现水平组合，axis=1
print hc1
print "-----------垂直组合-----------"
vc = np.vstack((a,b))# 垂直组合
print vc
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0  2  4]
#  [ 6  8 10]]

vc1 = np.concatenate((a,b),axis=0)# concatenate也能实现垂直组合，axis=0，或者不写
print vc1
print "-----------深度组合-----------"
dc = np.dstack((a,b))# 深度组合 就是把a的第一个行的第一个和b的第一行的第一个生成一个新的一行
print dc
# [[[ 0  0]
#   [ 1  2]
#   [ 2  4]]
#
#  [[ 3  6]
#   [ 4  8]
#   [ 5 10]]]
print "-----------列组合-----------"
column_c = np.column_stack((a,b))# 列组合 二维数组的列组合效果等同于水平组合
print column_c

print "-----------行组合-----------"
row_c = np.row_stack((a,b))# 行组合  二维数组的行组合效果等同于垂直组合
print row_c
print row_c == vc