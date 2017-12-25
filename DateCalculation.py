# -*- coding: utf-8 -*-

year = int(raw_input("请输入年份:"))
month = int(raw_input("请输入月份:"))
day = int(raw_input("请输入日期:"))
count = 0
leap = False
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = True
if (leap and month > 2):
    count += 1
if (month > 7):
    count += ((month-8)/2*31 + (month-8)/2*30 + (month-8)% 2 * 31+day + 3*61+28)
elif(month >2 and month < 8):
    count += ((month - 1) / 2 * 31 + (month - 1) / 2 * 30 + ((month - 1) % 2) * 31 + day -2)
else:
    count += ((month -1)*31+day)
print count