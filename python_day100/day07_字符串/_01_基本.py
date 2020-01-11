"""
    @Author fxiong
    @Date 2020/1/10 10:46
    @Describe 
    @Version 1.0
"""
#倍数增加
s1 ='hello'*3
print(s1)
#字符串拼接
s2 = 'word'
s1 += s2
print(s1)
# 包含判断
print('ll' in s1)
#不包含判断
print('word' not in s1)
#获取指定下标的字符
str = 'abc123546'
print(str[3])
#字符串切片（指定索引开始到指定索引结束）
print(str[2:5])
print(str[3:])
print(str[:4])
#隔断取值
print(str[3::2])
#前面不写边上默认从0开始
print(str[::2])
#可进行字符串倒序
print(str[::-1])
#反向切去
print(str[-3:-1])