"""
    @Author fxiong
    @Date 2020/1/10 12:50
    @Describe 
    @Version 1.0
"""
list1 = [1,2,5,977,66]
#添加元素
list1.append(500)
list1.insert(3,555)
print(list1)
#合并列表
list1.extend([888,777])
print(list1)
list1+=[145,256]
print(list1)
#判断元素是否存在列表中，若存在则删除该元素
if 977 in list1:
    list1.remove(977)
print(list1)
#移出指定位置的元素
list1.pop(4)
print(list1)
#清空列表
list1.clear()
print(list1)