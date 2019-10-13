#继承性   2019-8-28
from m4 import Human
class Student(Human):
    
    def __init__(self,school,name,age):
        self.school=school
       
        #调用父类的构造函数  需要加入self   方式一
        Human.__init__(self,name,age)
        #方式二  使用super关键字
        super(Student,self).__init__(name,age)
    
    def out(self):
        #调用父类方法
        super(Student,self).show()
        print("加油")

    #如果

ss =  Student('社会','44',5)

print(ss.name)
print(ss.age)
ss.out()
