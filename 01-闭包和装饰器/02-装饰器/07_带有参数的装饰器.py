
def return_decorate(flag):
    def decorator(func):
        def inner(a, b):
            if flag == "+":
                print("正在努力执行加法计算。。。。")
            elif flag == "-":
                print("正在努力执行减法计算。。。。")
            func(a, b)

        return inner
    return decorator


# 加法计算
@return_decorate("+")
def add_num(a, b):
    result = a + b
    print(result)


# 减法计算
@return_decorate("-")
def minus_num(a, b):
    result = a - b
    print(result)


add_num(12, 90)
minus_num(45, 3)

# 带有参数的装饰器，其实就是定义了一个函数，让函数接收参数，在函数内部返回的是一个装饰器
