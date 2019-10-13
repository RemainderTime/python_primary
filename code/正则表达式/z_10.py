# 使用函数替换操作
import re
a='PythonC#Java'

#函数
def show(value):

    #打印出来的是一个对象
    #print(value)
    #获取集体的值
    matched = value.group()
    return "!!"+matched+"!!"

r = re.sub('C#',show,a,1)

print(r)