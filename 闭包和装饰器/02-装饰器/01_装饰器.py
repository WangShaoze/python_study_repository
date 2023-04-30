# 学习目的：对已有的函数就行额外功能的扩展，装饰器本质上是一个闭包函数，也就是一个函数嵌套

# 装饰器的特点:
# 1. 不修改已有函数的源代码
# 2. 不修改已有函数的调用方式
# 3. 给以后函数添加额外的功能


# 定义装饰器
def decorator(func):  # 如果闭包函数的参数只有一个且是函数类型，那么这个闭包成为装饰器

    def inner():
        # 在内部函数里面对已有函数进行装饰
        print("已添加登录验证")
        func()

    return inner


def comment():
    # print("已添加登录验证")
    print("发表评论")


"""
已添加登录验证
发表评论
"""

# 调用装饰器对已有函数进行装饰
comment = decorator(comment)

# 调用方式不变
comment()
