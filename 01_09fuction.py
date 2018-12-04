#定义了一个函数
def sum_2_nums():
    a = 10
    b = 20
    result = a + b
    sesult = str("%d+%d=%d"%(a,b,result))
    print(result)

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
sum_2_nums()

