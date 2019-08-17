Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ord('dd')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ord('dd')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('d')
100
>>> [1,23,1]>[4,5,6]
False
>>> (7,5,6)<(8,5,4)
True
>>> print("逻辑运算符")
逻辑运算符
>>> 1 and 1
1
>>> 'c' or '2'
'c'
>>> not 4
False
>>> not []
True
>>> not [1,5]
False
>>> [] and [4,5]
[]
>>> 'c' and []
[]
>>> [] and '2'
[]
>>> 'd' and
SyntaxError: invalid syntax
>>> 'd' and ''
''
>>> [] and ''
[]
>>> [] or 'd'
'd'
>>> [] or ''
''
>>> 5 or 4
5
>>> print('成员运算符')
成员运算符
>>> a=1
>>> a in [1,2,3]
True
>>> b= '5'
>>> b not in (4,'5',4)
False
>>> b not in {4,'5',4}
False
>>> c=5
>>> c in {'2':4,5:4}
True
>>> print("身份运算符")
身份运算符
>>> 1 is 2
False
>>> a=4
>>> b=4
>>> a is b
True
>>> 1 == 1.0
True
>>> a is 1.0
False
>>> print("思考题")
思考题
>>> a ={1,2,3}
>>> b ={3,2,1}
>>> c =(1,2,3)
>>> d =(3,2,1)
>>> a==b
True
>>> a is b
False
>>> c ==d
False
>>> c is d
False
>>> a= 5
>>> type(a) == int
True
>>> isinstance(a,str)
False
>>> isinstance(a,int)
True
>>> isinstance(a,(int,float,str))
True
>>> print("位运算符")
位运算符
>>> a=2
>>> b=3
>>> a & b
2
>>> a | b
3
>>> 
