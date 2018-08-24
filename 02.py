#_*_ coding:utf-8 _*_
# 条件判断
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('your age is',age)
    print('teenager')

birth = int(input('birth:'))
if birth<2000:
    print('00前')
else:
    print('00后')