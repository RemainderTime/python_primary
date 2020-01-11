#第三个参数
import re
a='PythonC#Java'

#.号匹配任何字符包括换行符 \n
#r=re.findall('C#.{1}',a,re.I)
# re.I 表示忽略大小写   re.S 表示改变.号的行为
r=re.findall('C#.{1}',a,re.I | re.S)
print(r)