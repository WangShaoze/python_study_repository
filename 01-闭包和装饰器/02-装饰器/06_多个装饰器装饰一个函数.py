
# 定义装饰器
def make_p(func):
    print("make_p 装饰器执行了")

    def inner():
        # 在内部函数对函数进行装饰
        resu = "<p>"+func()+"</p>"
        return resu

    return inner


# 定义装饰器
def make_div(func):
    print("make_div 装饰器执行了")

    def inner():
        # 在内部函数对函数进行装饰
        resu = "<div>"+func()+"</div>"
        return resu

    return inner


# 多个装饰器的过程，由内到外的装饰
# 原理剖析  content = make_div(make_p(content))
@make_div
@make_p   # content = make_p(content)  content = inner
def content():
    return "Python"


# <p>Python<p>
result = content()
print(result)
