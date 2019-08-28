#面向对象
#类，对象
#实例化
#类最基本的作用：封装

#构造函数

class Student():
    name = '77'   #类变量
    sum = 5
    source=0
    __test=2
 
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

#无法进行私有变量调用，因为python的动态机制，这里其实是中心定义了一个变量__test
#原来的变量编程了 类名加变量名  如：_Student__test
student.__test=2
print(student.__test)
print(student.__dict__)


#调用类变量 方式2
print(Student.name)  

student.marking(22)