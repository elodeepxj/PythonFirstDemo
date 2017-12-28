# -*- coding:utf-8 -*-
import datetime
# 将日期转换成星期，0~6，周一~周日
def datestr2num(s):
    return datetime.datetime.strptime(s,"%d-%m-%Y").date().weekday()