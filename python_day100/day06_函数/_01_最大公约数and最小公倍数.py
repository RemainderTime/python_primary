"""
    @Author fxiong
    @Date 2019/12/31 16:07
    @Describe 函数的使用
    @Version 1.0
"""

def ged(x,y):
    if x > y:
        (x,y) = (y,x)
    for divisor in range(x,0,-1):
        if x % divisor == 0 and y % divisor == 0:
            return divisor

def gbs(x,y):
    return x*y//ged(x,y)

x = int(input('x='))
y = int(input('y='))
print('%d和%d最大公约数%d' % (x,y,ged(55,66)))
print('%d和%d最小公倍数%d'% (x,y,gbs(55,66)))