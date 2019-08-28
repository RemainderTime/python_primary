#继承父类  2019-8-28
class Human():

    sum = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("父类的方法")
    