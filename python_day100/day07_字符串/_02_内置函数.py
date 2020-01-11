"""
    @Author fxiong
    @Date 2020/1/10 11:02
    @Describe 
    @Version 1.0
"""
str = 'hello world!'
#通过内置函数len()计算字符串的长度
print(len(str))
#获取字符串首字母大写的拷贝
print(str.capitalize())
#获取字符串中每个单词的手字母大写的拷贝
print(str.title())
#获取字符串中每个字母的大写拷贝
print(str.upper())
#查找字符串中子串的位置索引（字符串中未找到子串则返回-1）
print(str.find('or'))
print(str.find('dd'))
#另一种查找子串所有的函数（字符串中未找到子串则会引发异常）
# print(str.index('or'))
# print(str.index('dd'))
#查找字符串是否为指定的字符串开头（区分大小写）
print(str.startswith('He'))
print(str.startswith('he'))
#查找字符串是否为指定的字符串结束（区分大小写）
print(str.endswith('D!'))
print(str.endswith('d!'))
#将字符串已指定的宽度居中并在两侧填充指定的字符
print(str.center(50,'$'))
#将字符串已指定的宽度靠右并在左边填充指定的字符
print(str.rjust(50,' '))
#
str2 = 'abc123456'
#判断字符串是否都由数字组成
print(str2.isdigit())
#判断字符串是否都由字母组成
print(str2.isalpha())
#判断字符串是否由字母和数字组成
print(str2.isalnum())
#
str3 = '  remaindertime@gemil.com   '
print(str3)
#获取去除两边空格的字符串的拷贝
print(str3.strip())
