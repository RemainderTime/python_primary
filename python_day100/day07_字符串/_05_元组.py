"""
    @Author fxiong
    @Date 2020/1/10 13:48
    @Describe 
    @Version 1.0
"""
import sys
#元组和列表差不多，只是元组中的元素不能进行修改操作
t = (11,'哈哈',True,'remaindertime')
print(t)
#获取元组的元素
print(t[1])
print(t[2])
#遍历元组
for member in t:
    print(member)
#给元组中的元素重新赋值
# t[2] = 44  #异常
#将元组转换成列表
list = list(t)
print(list)
#列表可进行修改
list[2] =444
print(list)
#将列表转换成元组
tu = tuple(list)
print(tu)
#比较元组和列表储存相同的元素所占用的内存
l = [1,2,3,3]
tt =(1,2,3,3)
print(sys.getsizeof(l))
print(sys.getsizeof(tt))