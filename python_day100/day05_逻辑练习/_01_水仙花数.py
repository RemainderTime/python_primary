"""
    @Author fxiong
    @Date 2019/12/31 14:55
    @Describe 
    @Version 1.0
"""
"""
python range() 函数可创建一个整数列表，一般用在 for 循环中
"""
for num in range(100,1000):
    x = num % 10
    y = num // 10 % 10
    z = num // 100
    if x**3 + y**3 + z**3 == num:
        print('%d为水仙花数' % num)
