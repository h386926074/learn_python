#定义了一个函数

a = 100   #一般会加一个g_a 表示是一个全局变量

def sum_2_nums():
    global a #想修改全局变量a  添加global 前缀  如果只是调用取值 不用添加
    a = 10
    b = 20
    result = a + b
    sesult = str("%d+%d=%d" % (a, b, result))
    print("a = %d"%a)
    print(sesult)

def test():
    print("a = %d"%a)


#
# num1 = int(input("请输入第一个数字："))
#
# num2 = int(input("请输入第二个数字："))
#
# sum_2_nums()
# test()

#定义一个全局变量  如果在函数中调用使用的话,可以直接使用 如果想要修改全局变量的值\
# 可以在函数中给变量使用global前缀
# 但是列表和字典除外  定义的列表和字典全局变量  在函数中可以直接调用和修改不用添加global 前缀

#python 多个返回值 默认返回的是一个元组   如果加了[]  返回的是一个数组

def moreReturnValue():
    a,b,c = 1,2,3
    print(a,b,c)
    return [a,b,c]

print(type(moreReturnValue()))#可以通过type 来查看一个变量的类型

def str_reduce():
    """对字符串进行反转"""
    a = "abcdefg"
    b = a[::-1]
    # a[i:j:s] 字符串或数组切片 i默认是0 j默认是len(a)  s表示步进 默认是1
    # 当s为负数时 i缺省默认表示-1 j缺省默认是-len(a)-1
    # b = a[::-1] 所以这个表示 b等于把a 从后到前 复制了一份  反转
    print("\n"+a+"\n"+b)

# str_reduce()

def default_argument(a,b=20,c=30):
    """缺省参数写法"""
    #b和c 默认可以不传
    #类似 default_argument(20) default_argument(20,30,40)
    # default_argument(20,c=30) 这个参数 a=20,b = 20 c=30
    # 可以跳过b 调用时只传 a 和 c  实例 print("ccc",end="")  \

#def default_args(a,b,*args):
#    这种定义的参数  使用传参时 可以是无限多个 但最多有两个参数,前两个传a 和b
#    剩下的传到args 元组    (33,)元组只有一个元素时一定要加"," 否则不能称之谓元组   \


