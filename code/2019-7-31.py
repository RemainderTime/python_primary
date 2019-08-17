Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> （1,2,3,4，9，8）*8
SyntaxError: invalid character in identifier
>>> （1,2,3）
SyntaxError: invalid character in identifier
>>> (1,1,2,2)
(1, 1, 2, 2)
>>> (1,2,5,3)* 4
(1, 2, 5, 3, 1, 2, 5, 3, 1, 2, 5, 3, 1, 2, 5, 3)
>>> type((1,2,3))
<class 'tuple'>
>>> type((1))
<class 'int'>
>>> type(('ddd'))
<class 'str'>
>>> 3 in [1,2,3,4]
True
>>> 3 not in [1,2,5,6,4]
True
>>> len('dgdgdgd')
7
>>> max([5,6,4,8,9])
9
>>> min([8,5,6,23,1])
1
>>> max('dfdssgsa')
's'
>>> min('derrerhsvx')
'd'
>>> ord('f')
102
>>> 
