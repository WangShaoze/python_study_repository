# property属性
### 1.property属性_**装饰器**方式使用
**代码块:**
```python
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
```
### 2.property属性_**类属性**方式使用
**代码块:**
```python
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
```