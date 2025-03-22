"""
类装饰器
"""


class Logger:
    def __init__(self, func: type = print):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("开始执行...")
        rsl = self.func(*args, **kwargs)
        print("结束执行...")
        return rsl


@Logger  # inner = Logger(test)  ===> test = inner ===> test(11, 12)  ===> inner(11,12)
def test(n, m):
    return n * m


if __name__ == '__main__':
    print(test(11, 12))
    # logger = Logger()
    # logger()  # ===> 像函数一样使用类的对象
