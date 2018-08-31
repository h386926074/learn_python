# _*_ coding:utf-8 _*_
#循环
names = ['michael','bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart','Lisa','Adam']
for s in L:
    print('Hello,%s!' % s)
    print('Hello,{}'.format(s))

n = 1
while n<=100:
    print(n)
    n=n+1
print('END')

n = 1
while n<100:
    if n>10:
        break
    print(n)
    n = n+1
print('END')

m = 0
while m < 100:
    m = m + 1
    if m % 2 == 0:
        continue
    print(m)

