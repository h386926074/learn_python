# _*_ coding:utf-8 _*_
from urllib.request import urlopen

from bs4 import BeautifulSoup

html_test = urlopen()
html = urlopen('http://jr.jd.com')

bs_obj = BeautifulSoup(html.read(), 'html.parser')

text_list = bs_obj.find_all('a','nav-item-primary')

for text in text_list:
    print(text.get_text())

html.close()
