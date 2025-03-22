# 闭包: 词法环境 + 函数嵌套

"""
闭包的形成需满足以下条件：
    嵌套函数：内部函数定义在外部函数内部。
    变量引用：内部函数引用了外部函数的变量（自由变量）。
    返回内部函数：外部函数将内部函数作为返回值返回。
"""


def outer(n):
    def inner(q):
        print(n * q)

    return inner


if __name__ == '__main__':
    inner_fun = outer(10)

    for u in range(10):
        inner_fun(u)
