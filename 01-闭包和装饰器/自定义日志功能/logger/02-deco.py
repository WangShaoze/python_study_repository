"""装饰器: 一个特殊的闭包"""


def outer(func: type):
    def inner(n):
        print("test start ...")
        func(n)
        print("test end ...")

    return inner


@outer  # <===> inner = outer(test)   ===> test = inner  ===> test = outer(test)  ===> test(n) ===> inner(n) ===> print("test start ...")  ===> print(n * 10) ===> print("test end ...")
def test(n):
    print(n * 10)


if __name__ == '__main__':
    test(8)
