#-*- coding:utf-8 -*-
print("Hello world")
print("well water"+"river")
print('I l"ove" huangfeng')
temp = input("现在想的什么数字：")
guess = int(temp)
if guess == 8:
    print("我草，？！")
else:
    print("haha")
print("游戏结束")
print ('Let"s go!')
strss=r'C:\now'
print(strss)
strss = '''dklsafjkldajsl;fjlsd
sd;fksjfjklsj;af
dsklaf;jkldsallfkja
dskl;fjkladsf
dsakf;jkads;
dskl;a
'''
print (strss)
#float() 将一个 字符串 或 整数 转化为 浮点数
#type() 输出一个变量的类型
#isinstance(520,int)  判断一个变量的类型是不是某类型， 返回bool
# python3  "/" 除法表示 真实的除法 带小数  如果想用取余商的用法 使用 '//'
# 3 ** 2  幂运算 结果9
# 逻辑操作符
# 幂运算 比 左侧的优先级高 比右侧的优先级低
# -3 ** 2 = -（3**2）=-9     3 ** -2= 3**（-2）= 0.11111111
print("oneto")
#ord('a') 获取字符的整数表示   chr() 函数把编码转换为对应的字符
ord('A')   # 结果为 65
chr(66)  #'B'
'\u4e2d\u6587'
strr = 'Hello,%s,%s' % ('world','very good')  #字符串格式化 ，一个参数时括号可以省略
print(strr)
# %d 整数   %s 字符串   %f 浮点数   %x  十六进制整数

#另一个种格式化字符串的方法 format()

#list
classmates = ['michael','Bob','Tracy']   #len() 获取list 个数  下标获取单个元素

#换取 list 最后一个元素
print(classmates[len(classmates)-1])
classmates.append('Admin') #追加元素到末尾
classmates.insert(1,'Joey')  #插入元素到指定位置
print(classmates)
classmates.pop()  #删除list末尾的元素   也可以指定位置
classmates.pop(0)
print(classmates)
classmates[0] = 'Search'    #替换某个元素q

#list 里面的元素 也可以是另一个list
s = ['python','java',classmates]
print(s)

#tuple 和list 很相似  元组   ，只是元组一旦初始化就不能修改
classtuple = ('Michael','Bob','Tracpy')
print(type(classtuple))