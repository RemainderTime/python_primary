#参数
#1.必须参数
#2.关键字参数
#3.默认参数

def add(a,b):
    print(a,b)

add(3,1)

#2.关键字参数
add(b=8,a=9)

#3.默认参数
def show(age=20,name='小米',sex='男'):    
    print('age:'+str(age))
    print('name:'+name)
    print('sex:'+sex)

show(age=22)

def cc(collage,age=20,name='小米',sex='男'):    #必须把必须参数放入默认参数前面 ，不能混用
    print('collage:'+str(collage))  
    print('age:'+str(age))
    print('name:'+name)
    print('sex:'+sex)

cc(20)