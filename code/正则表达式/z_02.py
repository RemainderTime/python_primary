
#字符集
import re

a='abc,abd,acc,abd,asd'

r=re.findall('a[cb]d',a)
s=re.findall('a[^cb]d',a)
print(r)
print(s)