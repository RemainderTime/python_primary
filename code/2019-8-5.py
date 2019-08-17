Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type({1,2,3,5})
<class 'set'>
>>> {1,2,3,4,5}-{3,4}
{1, 2, 5}
>>> {1,2,3,4,5}&{3,4}
{3, 4}
>>> {1,2,3,4,5}|{3,4,7}
{1, 2, 3, 4, 5, 7}
>>> type(set())
<class 'set'>
>>> type({1:2,2:8,4:6})
<class 'dict'>
>>> {1:2,2:8,4:6}[2]
8
>>> 
