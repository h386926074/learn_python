#! /usr/bin/env python3
import random
secret = random.randint(1,10)
print('---------my my----------')
temp = input("猜数字1-10的随机数：")
guess = int(temp)
while guess != secret:
    temp = input("猜错了，请重新输入：")
    guess = int(temp);
    if guess == secret:
        print("这都能猜中")
        print("猜中也没啥")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("小了，小了~~~~")
print("游戏结束，不玩啦……")
