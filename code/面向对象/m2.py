#面向对象
#类，对象
#实例化
#类最基本的作用：封装

#构造函数

class Student():
    name = '77'   #类变量
    sum = 5
    source=0
 
     #构造方法
    def __init__(self,name):
        self.name=name
        self.source= 0
        print(name) #调用实例变量 方式1
        print(self.name) #调用实例变量 方式2
        print(self.__class__.name)#调用类变量 方式1

    #实例方法
    def show(self):  
        print("python")

    #类方法
    @classmethod  
    def plus_sum(cls):
        cls.sum +=1  #调用类变量
        print(cls.sum)

    #安全赋值
    def marking(self,source):
        if source<0:
            self.source=0
        self.source = source
        print('分数：'+str(self.source))




student = Student('哈哈')#实例变量
print(student.name)


#调用类变量 方式2
print(Student.name)  

student.marking(22)