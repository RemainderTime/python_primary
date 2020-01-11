import re

s = 'int sdf= dfd d, python , i love java'

#使用组匹配  ()  ,可以多个组
r = re.findall('int(.*)python(.*)java',s)

#print(r.group(1,2))
#获取全部组
print(r.groups())
