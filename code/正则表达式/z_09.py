#
import re
a='PythonC#Java'
#替换   1表示只替换第一个 
r = re.sub('C#','GO',a,1)

#内置函数替换
b = a.replace("C#","GO")
print(b)

print(r)