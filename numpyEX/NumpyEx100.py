# -*- coding:utf-8 -*-

import numpy as np
from matplotlib.pyplot import plot, show

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
d, open, high, low, close = np.loadtxt("e:/PythonProjectSpace/data/data.csv", delimiter=',', usecols=(1, 3, 4, 5, 6),
                                       unpack=True, converters={1: Utils.datestr2num})
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
close = close[:16]
open = open[:16]
high = high[:16]
low = low[:16]
first_day = np.ravel(np.where(dates == 0))[0]
print "第一周的星期一:", first_day
last_day = np.ravel(np.where(dates == 4))[-1]
print "第三周的星期五", last_day
week_indexs = np.arange(first_day, last_day + 1)
week_indexs = np.split(week_indexs, 3)
print week_indexs


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]  # 周开盘价就是周一开盘价
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]  # 周收盘价就是周五收盘价
    return ("APPLY", monday_open, week_high, week_low, friday_close)


weeksummary = np.apply_along_axis(summarize, 1, week_indexs, open, high, low, close)  # 获取周数据
print weeksummary

# 真实波动幅度均值
n = 15
h = high[-n:]
l = low[-n:]
print h
print l
pre_close = close[-n - 1:-1]
print pre_close
truerange = np.maximum(h - l, h - pre_close, pre_close - l)  # 多个数组中的最大值
atr = np.zeros(15)
atr[0] = np.mean(truerange)
for i in range(1, 15):
    atr[i] = (15 - 1) * atr[i - 1] + truerange[i]
    atr[i] /= 15
print atr

# 简单移动平均线\
n = 10
weights = np.ones(n) / n
print weights
sma = np.convolve(weights, close)[n - 1:-n + 1]
t = np.arange(n - 1, len(close))
print t
print sma
plot(t, close[n - 1:], lw=1.0)
plot(t, sma, lw=2.0)
show()
