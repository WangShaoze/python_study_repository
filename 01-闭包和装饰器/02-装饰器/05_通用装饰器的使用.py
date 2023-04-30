# 通用的装饰器可以装饰任意类型的函数
# ——————————————————————装饰带有参数的函数——————————————————————————

"""
def decorator(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型要和已有参数的类型保持一直
    def inner(num1, num2):
        # 在函数内部对已有函数进行装饰
        print("正在努力执行加法计算")
        func(num1, num2)

    return inner


@decorator   # 用装饰器语法糖装饰带有参数的函数
def add_num(num1, num2):
    result = num1 + num2
    print("结果为：", result)


add_num(1, 2)
"""


# ——————————————————————带有参数和返回值的函数进行装饰——————————————————————————
"""
def decorator(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型要和已有参数的类型保持一直
    def inner(num1, num2):
        # 在函数内部对已有函数进行装饰
        print("正在努力执行加法计算")
        resu = func(num1, num2)
        return resu

    return inner


# 用装饰器语法糖装饰带有参数的函数
@decorator   # add_num = decorator(add_num), add_num = inner
def add_num(num1, num2):
    resu = num1 + num2
    return resu


result = add_num(1, 2)
print("结果为：", result)
"""

# ——————————————————————对带有 不定长参数 和返回值 的函数进行装饰——————————————————————————
# 该装饰器就是一个通用的装饰器
def decorator(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型要和已有参数的类型保持一直
    def inner(*args, **kwargs):
        # 在函数内部对已有函数进行装饰
        print("正在努力执行加法计算")
        # *args: 把元组里面的每一个元素，按照位置顺序进行传参
        # **kwargs: 把字典里面的每一个键值对，按照关键字的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        resu = func(*args, **kwargs)
        return resu

    return inner


# 用装饰器语法糖装饰带有参数的函数
@decorator   # add_num = decorator(add_num), add_num = inner
def add_num(*args, **kwargs):
    resu = 0
    # args: 元组类型
    # kwargs: 字典类型
    for value in args:
        resu += value

    for value in kwargs.values():
        resu += value

    return resu


result = add_num(1, 2)
print("结果为：", result)


@decorator
def show():
    return "haha"


print(show())



