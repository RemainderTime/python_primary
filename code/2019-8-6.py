Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=[1,2,3,4]
>>> print(A)
[1, 2, 3, 4]
>>> A*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> B=[8,6,4]
>>> A*4+B
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 8, 6, 4]
>>> type=3
>>> print(type)
3
>>> a=1
>>> b=a
>>> a=5
>>> b
1
>>> a=[2,5,8]
>>> b=a
>>> a[0]='3'
>>> b
['3', 5, 8]
>>> a='dddgf'
>>> a=a+'555'
>>> a
'dddgf555'
>>> a=[12,56,88]
>>> id(a)
50499536
>>> hex(id(a))
'0x3028fd0'
>>> a=5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b=1
>>> b+=b>1
>>> b
1
>>> print(b+=b>1)
SyntaxError: invalid syntax
>>> b+=b>=1
>>> b=1
>>> b+=b>=1
>>> b
2
>>> 
