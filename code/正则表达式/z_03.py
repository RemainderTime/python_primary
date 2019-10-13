
#概括字符集
import re

#\d  数字 \D  非
#\w   单词字符   \W  非
# \s 空白字符   \S 非
a='5566dfd5fdg5gs26s0'

r=re.findall('[1-9]',a)
s=re.findall('[^0-9]',a)
f=re.findall('\w',a)
print(r)
print(s)
print(f)