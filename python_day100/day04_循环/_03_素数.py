"""
    @Author fxiong
    @Date 2019/12/31 14:10
    @Describe 
    @Version 1.0
"""
from  math import sqrt

num = int(input("请输入一个正整数:"))
flag = True
for x in range(2,num):
    if num % x == 0 :
        flag = False
        break;
if flag and num != 1:
    print('%d是素数'%num)
else:
    print('%d不是素数' % num)