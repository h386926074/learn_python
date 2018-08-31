# _*_ coding:utf-8 _*_
#function
r1 = 12.34
r2 = 9.08
r3 = 73.1

s1 = 3.14 * r1 *r2
pi = abs(s1)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-6))

age = 2
if age >= 18:
    pass


def my_abs_01(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs_01(-5)

# ax*2 + bx + c = 0
import math

math.sqrt(2)  # 求平方根

def power(x,n=2):   #参数可以设置 默认值  power(x,n=2)
    s = 1
    while n>0:
        n = n - 1
        s = s *x
    return s
print(power(2,3))
print(power(2))

def enroll(name,gender,age=6,city='shiyan'):
    print('name:',name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('huangfeng','F')

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())

# 三元操作符
x,y = 4,5
small = x if x<y else y
print(small)