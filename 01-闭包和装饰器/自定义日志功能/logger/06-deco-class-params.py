"""
带参数的类装饰器
2025-3-17 00:00:00  ====> "%Y-%m-%d %H:%M:%S"
@Logger("%Y-%m-%d %H:%M:%S")

logger = Logger("%Y-%m-%d %H:%M:%S") ===> @logger

@logger ===> inner = logger(hello) ===> hello = inner ===> hello() ===> inner()

logger()  将对像像函数一样使用
"""

import time


class Logger:
    def __init__(self, time_format="%Y-%m-%d %H:%M:%S"):
        self.time_format = time_format
        self.func = None

    def inner(self, name):
        print("{} 开始执行...".format(time.strftime(self.time_format)))
        rsl = self.func(name)
        print("{} 结束执行...".format(time.strftime(self.time_format)))
        return rsl

    def __call__(self, func: type):
        self.func = func
        return self.inner


@Logger("%Y-%m-%d %H:%M:%S")
def hello(name):
    print("Hello %s!" % name)


@Logger("%Y/%m/%d %H:%M:%S")
def hi(name):
    print("Hello %s!" % name)


if __name__ == '__main__':
    hello("Lilio")
    print("#" * 100)
    hi("Lilio")
