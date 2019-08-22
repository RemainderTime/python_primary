#面向对象
#类，对象
#实例化
#类最基本的作用：封装

#构造函数

class Student():
    name = '77'

    def __init__(self,name):
        self.name=name

    def show(self):
        print("python")

student = Student('哈哈')
print(student.name)