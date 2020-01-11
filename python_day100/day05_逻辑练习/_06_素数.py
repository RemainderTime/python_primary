"""
    @Author fxiong
    @Date 2019/12/31 15:34
    @Describe 查找100以内的素数
    @Version 1.0
"""
arr = list()
for num in range(2,100):
    flag = True
    for x in range(2,num):
        if num % x == 0 :
            flag = False
    if flag and num != 1:
        arr.append(num)
print('100以内的素数有：', arr)
