#_*_ coding:utf-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup

base = 'http://www.biquge.com.tw/18_18698/'
html = urlopen(base)

zm_obj = BeautifulSoup(html.read(),'html.parser')

zm_div = zm_obj.find('div',id='info')


print(zm_div,type(zm_div))

for child in zm_div:
    print(child.string)
# 对BeautifulSoup 库没有深入学习
# 未完成

