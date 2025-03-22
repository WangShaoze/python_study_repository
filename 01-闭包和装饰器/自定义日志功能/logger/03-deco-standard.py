""" 标准的装饰器是如何定义的？
1.没有正确处理返回值
2.参数传递存在局限性
"""


def outer(func: type):
    def inner(*args, **kwargs):
        print("test start ...")
        rsl = func(*args, **kwargs)
        print("test end ...")
        return rsl
    return inner


@outer  # inner = outer(add)  ===> add = inner  ===> add(12, 13)  ===> inner(12, 13)
def add(n, m, x, y=10, z=11):
    return sum([n, m, x, y, z])


def add2(n, m, x, b, c, y=10, z=11):
    return sum([n, m, b, c, x, y, z])


if __name__ == '__main__':
    print(add(12, 13, 4, y=1, z=7))

    print(add2(1, 2, 4, 5, 6, 7, 4))
