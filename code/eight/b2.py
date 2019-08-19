#函数
#def funcname()

import sys
sys.setrecursionlimit(100000)

def add(x,y):
    result=x+y
    return result

def printa(code):
    print(code)


a=add(1,2)
printa('python')

print(a)