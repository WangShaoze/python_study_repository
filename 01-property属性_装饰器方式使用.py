class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 34

    @property  # 当对象调用age方法时可以像调用属性一样调用
    def age(self):
        return self.__age

    @age.setter   # 可以使设置属性的方法,直接使用赋值实现
    def age(self, new_age):
        if (new_age > 0) and (new_age < 135):
            self.__age = new_age
        else:
            print("年龄不合法!!")

"""
提示: 使用装饰器的方式使用property属性使,被装饰的方法名必须相同
"""

student = Student()
# age = student.age()
print(student.age)

student.age = 45
print(student.age)

student.age = 136
print(student.age)
