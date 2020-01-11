
#数量词
#*  匹配0次或者无限次
#？  匹配0次或者1次
#+  匹配1次或者无限次
import re

a='pytho5python4pythonn2'

r=re.findall('python?',a)
r2=re.findall('python*',a)
r3=re.findall('python+',a)

print(r)
print(r2)
print(r3)

