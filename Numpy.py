#!/Python27/python
# -*- coding:utf_8 -*-;

import numpyEX as np
print np.__version__;
print "----------------抢镜的分割线再次出现-------------------";
z = np.zeros(10);
z[4] = 1;
print z;
#[ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]
print "----------------抢镜的分割线再次出现-------------------";
y = np.arange(10,20)
print y;
#[10 11 12 13 14 15 16 17 18 19]
print "----------------抢镜的分割线再次出现-------------------";
x = np.arange(20)
print x[::-1];
# [19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0]

print "----------------创建一个3x3矩阵，取值范围从0到8-------------------";
v = np.arange(9).reshape(3,3)
print v;
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# for i in range(len(v)):
#     for j in range(len(v[i])):
#         print v[i,j]

print "----------------获取非零数字的位置-------------------";
nz = np.nonzero([1,2,0,0,3,4,0,5])
print nz;
# (array([0, 1, 4, 5, 7], dtype=int64),)
# 获取非零数字的位置

print "----------------创建一个3x3的矩阵-------------------";
z = np.eye(3)
print z;
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
#创建一个3x3的矩阵

print "----------------创建一个带有随机值的3x3x3数组-------------------";
z = np.random.random((3,3,3))
print z;

print "----------------创建一个带有随机值的10x10数组，并找到最小值和最大值-------------------";
z = np.random.random((10,10))
print z;
zmin,zmax = z.min(),z.max()
print zmin;
print zmax;

print "----------------创建一个30大小的随机向量，并找到平均值-------------------";
z = np.random.random(30)
print z.mean()

print "----------------在边框上创建一个2d数组，在里面创建一个0-------------------";
z = np.ones((10,10))
print z;
z[1:-1,1:-1] = 0;
print z;

print "----------------下列表达式的结果是什么?-------------------";

z = 0 * np.nan
y = np.nan == np.nan
x = np.inf > np.nan
u = np.nan - np.nan
v = 0.3 == 3 * 0.1
print z,y,x,u,v;

print "---------------创建一个5x5矩阵，它的值为1、2、3、4，刚好在对角线以下------";
z = np.diag(1+np.arange(4),k=-1)#k控制行数，负数为在原来矩阵上面创建K条数据，正数在原来矩阵下面创建K条数据,K=0就不创建
print z;


print "---------------创建一个8x8矩阵，并将其填充到一个棋盘格模式------";
z = np.ones((8,8),dtype=int);
z[1::2,::2] = 0;
z[::2,1::2] = 0;
print z;

print "---------------考虑一个(6,7,8)形状数组，第100个元素的索引(x,y,z)------";
print np.unravel_index(100,(6,7,10))#(x,y,z)x最大为6，y最大为7，z最大为10,100为第几个数组

print "---------------使用tile函数创建一个checkerboard 8x8矩阵------";
z = np.tile(np.array([[0,1,2],[2,1,0]]),(4,3))
print z;
#np.tile(np.array([a,b]),(x,y))  创建一个a*y列数,b*y列数,x组的矩阵
# a*y  \
#       x组
# b*y  /

print "---------------使一个5x5随机矩阵标准化------";
z = np.random.random((2,2))
zmax,mzin = z.max(),z.min();
z = (z-zmin)/(zmax - zmin)
print z;









