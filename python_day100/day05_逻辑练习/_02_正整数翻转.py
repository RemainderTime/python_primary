"""
    @Author fxiong
    @Date 2019/12/31 15:00
    @Describe 
    @Version 1.0
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)