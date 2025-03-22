"""带有参数的装饰器"""
""" 2025-3-17 00:00:00  ====> "%Y-%m-%d %H:%M:%S" """
""" 2025年3月17日 00时00分00秒  """
import time


def logger(time_formater: str):
    def outer(func: type):
        def inner(*args, **kwargs):
            print("{} 执行开始 func".format(time.strftime(time_formater)))
            rsl = func(*args, **kwargs)
            print("{} 执行结束 func".format(time.strftime(time_formater)))
            return rsl

        return inner

    return outer


# outer = logger("%Y-%m-%d %H:%M:%S") ===> @outer ===> inner = outer(hello) ===> test = inner
#  ===> test(name) ===> inner(name)  ===>  func(name)
@logger("%Y-%m-%d %H:%M:%S")
def hello(name: str):
    print("你好,{}".format(name))


@logger("%Y/%m/%d %H:%M:%S")
def hi(name: str):
    print("你好,{}".format(name))


if __name__ == '__main__':
    hello(name="LiLio")
    hi(name="阿甘")
