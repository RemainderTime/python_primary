"""
    @Author fxiong
    @Date 2019/12/31 14:35
    @Describe 
    @Version 1.0
"""

x = int(input('x='))
y = int(input('y='))
if x > y:
    x, y = y, x

for divisor in range(x, 0, -1):
    if x % divisor == 0 and y % divisor == 0:
        print('%d和%d的最大公约数为%d' % (x,y,divisor))
        print('%d和%d的最小公倍数为%d' % (x, y,x*y//divisor))
        break