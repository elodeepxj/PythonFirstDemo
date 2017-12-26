# -*- coding:utf-8 -*-

def add_end(L=None):#参数是可变的，需用none这个不变对象来实现
    if L is None:
        L=[]
        L.append("END")
    return L
def calc(*numbers):#多参数前面加*星号
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

def func(a,b,c=0,*args,**kw):#a,b是必选参数，c是默认参数，*args是可变参数（元祖），**kw是关键字参数（字典）
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

func(5,2)
func(5,2,1,'L','O','V','E',{'name':'Joker'})
# print calc(1,2,3)