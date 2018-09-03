#_*_ coding:utf-8 _*_
from selenium import webdriver

import csv  #导入csv 版块


#csv 读取
csv_file = csv.reader(open('playlist.csv','r'))
print(csv_file)

for stu in csv_file:
    print(stu)

stu1 = ['Marry',26]
stu2 = ['Bob',23]

out = open('playlist.csv','a',newline='')
csv_write = csv.writer(out)
csv_write.writerow(stu1)
csv_write.writerow(stu2)

print('write over')

