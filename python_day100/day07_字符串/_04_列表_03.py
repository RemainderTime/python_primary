"""
    @Author fxiong
    @Date 2020/1/10 12:50
    @Describe 
    @Version 1.0
"""
language = ['java','html','js','python']
language+=['go','c','c++']
print(language)
#列表切片
language1 = language[1:3]
print(language1)
#通过完整切片来复制列表
language2=language[:]
print(language2)
language3=language[-3:-1]
print(language3)
#通过反向切片来获得列表的拷贝（倒转列表）
language4=language[::-1]
print(language4)
#
arr = ['java','html','js','python']
#sorted函数返回列表排序后的拷贝不会修改传入的列表
list = sorted(arr)
print(list)
list1 = sorted(arr,reverse=True)
print(list1)
## 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list2=sorted(arr,key=len)
print(list2)
# 给列表对象发出排序消息直接在列表对象上进行排序
arr.sort(reverse=True)
print(arr)