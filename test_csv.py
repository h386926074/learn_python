#_*_ coding:utf-8 _*_
import csv

stu1 = ['Marry',26]
stu2 = ['Bob',23]

out = open('playlist01.csv','w',newline='')
csv_wirte = csv.writer(out)

csv_wirte.writerow(stu1)
csv_wirte.writerow(stu2)
out.close()

csv_reader = csv.reader(open('playlist01.csv','r',newline=''))

for stu in csv_reader:
    print(stu)


stud1 = ['huangfeng','test1']
csv_out_open = open('playlist01.csv','a',newline='')
csv_out = csv.writer(csv_out_open)
csv_out.writerow(stud1)
csv_out_open.close()

csv_reader = csv.reader(open('playlist01.csv','r',newline=''))

for stu in csv_reader:
    print(stu)

out1 = open('playlist02.csv','w',newline='')
csv_write01 = csv.writer(out1)   #添加动作属性 个人理解
student01 = ['This is the one number!']
csv_write01.writerow(student01)  #写入动作
out1.close()  #读取时候 可以没有关闭操作    写入完毕最好有关闭写入的动作 防止 下边再有操作的时候冲突

