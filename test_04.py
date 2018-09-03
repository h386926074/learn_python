# _*_ coding:utf-8 _*_
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://jr.jd.com')
# print(html.read())

bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all('a','nav-item-primary')

for text in text_list:
    print(text.get_text())

html.close()


html = urlopen('http://python.jobbole.com/89091/')
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find('div','entry-header')
print(text_list.h1.get_text())
html.close()

html = urlopen('http://10yan.com/')
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find('div','mainnav')
print(text_list)