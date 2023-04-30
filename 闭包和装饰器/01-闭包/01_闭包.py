# 闭包的作用： 可以保存外部函数的变量

# 外部函数
def func_out():   # ------> 可以传入参数
    num1 = 10

    def func_inner(num2):
        # 内部函数
        result = num1+num2
        print("结果是：", result)

    # 外部函数要返回内部函数，这个使用外部函数的变量的内部函数就叫做 01-闭包
    return func_inner   # 这里不可以加括号


# 获取闭包对象
# new_func 就是闭包
new_func = func_out()
# 执行闭包
new_func(1)
new_func(12)
"""
结果是： 11
结果是： 22
"""