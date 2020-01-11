"""
    @Author fxiong
    @Date 2019/12/31 15:24
    @Describe 找出10000以内的完美数
    @Version 1.0
"""

def fun1(num):
    list1 = []
    for i in range(1,num):
        if num % i ==0:
            list1.append(i)
    return list1
for num in range(1,10000):
    list2 = fun1(num)
    if sum(list2) == num:
        print(num,'是一个完美数,约数有',list2)
