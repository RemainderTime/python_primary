# 使用函数替换操作
import re
a ='Abc5566555'

#函数
def show(value):

    #打印出来的是一个对象
    #print(value)
    #获取集体的值
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return "5"

r = re.sub('55',show,a)

print(r)