
#数量词
import re

a='5566dfd5fdg5gs26s0'

r=re.findall('[a-z]{2,6}',a)
s=re.findall('[a-z]{2,6}?',a)
#贪婪  与 非贪婪
#python 默认贪婪
#非贪婪 后面加问号

print(r)

print(s)
