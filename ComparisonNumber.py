# -*- coding: utf-8 -*-
def twoNumber():
    number1= raw_input("请输入第一个数字：")
    number2= raw_input("请输入第二个数字：")
    if number1>number2:
        print number1,"大于",number2
    elif number2>number1:
        print number2,"大于",number1
    else:
        print number1,"等于",number2

def threeNumber():
    l = []
    for i in range(3):
        x = int(raw_input("请输入数字："))
        l.append(x)
    l.sort()
    print l[2],"大于",l[1],"大于",l[0]


type=int(raw_input("2个数字比较大小请输入2，三个数字比较大小请输入3。"))
if type == 2:
    twoNumber()
elif type ==3:
    threeNumber()
else:
    print "输入比较大小类型错误!"