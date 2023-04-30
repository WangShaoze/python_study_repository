class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 34

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if (new_age > 0) and (new_age < 135):
            self.__age = new_age
        else:
            print("年龄不合法!!")

    # 提供一个类属性,get_age 表示获取 __age 属性时执行的方法, set_age 设置 __age 的值时,执行的方法
    age = property(get_age, set_age)


student = Student()
student.age = 34
age = student.age
print(age)
