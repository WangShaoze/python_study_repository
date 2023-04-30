def func_out():
    num1 = 10

    def func_inner():
        # 在内部函数修改外部函数的变量
        # num1 = 20   # 表面上是修改实际上是：再闭包内部定义了一个变量

        nonlocal num1  # 需要使用 nonlocal 关键字，进行修改才是真正的方法
        num1 = 20
        # 内部函数使用外部函数的变量
        result = num1 + 10
        print(result)

    print("修改前的外部变量：", num1)
    func_inner()
    print("修改后的外部变量：", num1)

    return func_inner


new_func = func_out()
new_func()
