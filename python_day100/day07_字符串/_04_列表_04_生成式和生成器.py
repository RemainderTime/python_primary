"""
    @Author fxiong
    @Date 2020/1/10 12:50
    @Describe 
    @Version 1.0
"""
import sys
#用列表的生成表达式语法创建列表容器
h = [x for x in range(1,10)]
print(h)
#
h = [x+y for x in 'abcd' for y in '1234']
print(h)
#
h=[x**3 for x in range(1,1000)]
#查看对象占用的字节数
print(sys.getsizeof(h))
print(h)

