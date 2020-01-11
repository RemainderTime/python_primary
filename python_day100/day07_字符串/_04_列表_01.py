"""
    @Author fxiong
    @Date 2020/1/10 12:50
    @Describe 
    @Version 1.0
"""
list1 = [1,2,5,977,66]
print(list1)
#乘号表示列表的重复
list2 = ['hello']*3
print(list2)
#计算列表的长度
print(len(list1))
#下标索引
print(list1[2])
print(list1[4])
# print(list1[6])
#改变某个位置的值
list1[2] = 250
print(list1)
#通过下标变量列表元素
for index in range(len(list1)):
    print(list1[index])
#通过for变量列表
for elem in list1:
    print(elem)
#通过enumerate函数处理列表后遍历可以同时获得索引和元素
for index,elem in enumerate(list1):
    print(index,elem)
