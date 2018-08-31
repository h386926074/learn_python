# _*_ coding:utf-8 _*_
# 字典 和set
names = ['Michael','Bob','Tracy']
scores = [95,75,85]

d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
if d.get('jack',-1) == -1:
    print('d is not containes jack')

# 删除一个key 用pop
d.pop('Bob')
print(d)

#set
