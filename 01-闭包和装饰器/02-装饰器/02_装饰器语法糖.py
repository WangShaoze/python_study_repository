# 定义装饰器
def decorator(func):  # 如果闭包函数的参数只有一个且是函数类型，那么这个闭包成为装饰器

    def inner():
        # 在内部函数里面对已有函数进行装饰
        print("已添加登录验证")
        func()

    return inner


# 装饰器语法糖的写法： @装饰器的名称，
@decorator     # @decorator  <=============> comment = decorator(comment)
def comment():
    # print("已添加登录验证")
    print("发表评论")


comment()


# 装饰器的执行时机
# 当模块加载完成之后，装饰器就会立刻执行，对已有的函数进行装饰
