"""
    @Author fxiong
    @Date 2019/12/31 13:51
    @Describe 9X9剩法口诀
    @Version 1.0
"""

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()