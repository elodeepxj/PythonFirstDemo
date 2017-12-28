# -*- coding:utf-8 -*-

import numpy as np
import Utils

# 获取成交价和成交量
c, v = np.loadtxt("E:/PythonProjectSpace/data/data.csv", delimiter=',', usecols=(6, 7), unpack=True)

print "获取成交量加权平均价：", np.average(c, weights=v)
print "获取成交价平均值：", np.mean(c), np.average(c)
print "获取成交价差值:", np.ptp(c)

# 获取最高价和最低价
h, l = np.loadtxt("E:/PythonProjectSpace/data/data.csv", delimiter=',', usecols=(4, 5), unpack=True)
print "最高价的最大值：", np.max(h), "最低价的最小值：", np.min(l)
print "获取最高价和最低价的差值:", np.ptp(h), np.ptp(l)

print "获取成交价的中位数:", np.median(c)

# 分析收益率
print "获取成交价的收益率:", np.diff(c) / c[:-1]  # diff 相邻两个元素的差值构成的数组 除以前一天的价格
print "标准差：", np.std(np.diff(c) / c[:-1])
print "对数收益率：", np.diff(np.log(c))

print "收益率大于0的索引值：", np.where((np.diff(c) / c[:-1]) > 0)

volatility = np.std(np.diff(np.log(c))) / np.mean(np.log(c)) / np.sqrt(1. / 252.)
print "波动率:", volatility

# 日期分析
# 获取日期
d = np.loadtxt("e:/PythonProjectSpace/data/data.csv", delimiter=',', usecols=(1), converters={1: Utils.datestr2num})
print d

averages = np.zeros(5)  # 创建一个包含5个元素的数组，初始化元素都为0
print averages

for i in range(5):
    index = np.where(d == i)
    prices = np.take(c, index)
    avg = np.mean(prices)
    averages[i] = avg
    print i, "prices:", prices, "average:", avg
print np.max(averages), np.argmax(averages), np.argmin(averages)  # argmax获取最大值的索引值，argmin同理

# 汇总数据
dates = d[:16]
first_day = np.ravel(np.where(dates == 0))[0]
print "第一周的星期一:",first_day
last_day = np.ravel(np.where(dates == 4))[-1]
print "第三周的星期五",last_day
week_indexs = np.arange(first_day,last_day+1)
week_indexs = np.split(week_indexs,3)
print week_indexs
