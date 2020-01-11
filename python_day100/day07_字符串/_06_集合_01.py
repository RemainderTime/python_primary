"""
    @Author fxiong
    @Date 2020/1/10 13:48
    @Describe 
    @Version 1.0
"""
import sys
#集合中不能有重复的元素
set1 ={1,2,3,5,6,2,3}
print(set1)
print('length=%d' % len(set1))
#创建集合构造器语法
set2 = set(range(1,10))
set3 = set((1,2,5,6,455,4,5))
print(set2,set3)
#创建集合的推导式语法
set4 = {num for num in range(1,100) if num%3==0 or num%5==0}
print(set4)
#在集合中添加元素
set1.add(88)
set2.update([444,5555])
print(set1,set2)
#删除指定元素
set2.discard(3)
print(set2)
set1.pop()
print(set1)
