"""
    @Author fxiong
    @Date 2019/12/31 15:09
    @Describe 生成斐波那契数列的前20个数
    @Version 1.0
"""
arr = []
for i in range(20):
    if i == 0 or i == 1:
       arr.append(1)
    else:
        arr.append(arr[i-2]+arr[i-1])
print('斐波那契数列的前20个数为:', arr)
