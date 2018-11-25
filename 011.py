# _*_ coding:utf-8 _*_
from urllib import request

if __name__ == '__main__':
    response = request.urlopen('http://fanyi.baidu.com')
    html = response.read().decode('utf-8')
    print(html)