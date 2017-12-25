# -*- coding: utf-8 -*-
import random

number = random.randint(1,99)
guessNumber = int(raw_input("输入1——99中任意一个数字:"))
while True:
    if guessNumber < number:
        print "猜小了"
        guessNumber = int(raw_input("Enter an integer from 1 to 99: "))
    elif guessNumber > number:
        print "猜大了"
        guessNumber = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "恭喜你，猜对了！"
        break
