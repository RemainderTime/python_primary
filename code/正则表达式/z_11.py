import re
#其他函数匹配
s = 'C55ff55566'
r = re.match('\d',s)
print(r)
#获取匹配的位置
print(r.span())
r2 = re.search('\d',s)
print(r2)
#获取值
print(r2.group())

#与findAll不同之处为他们都只匹配一次