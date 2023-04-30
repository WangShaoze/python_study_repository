# 统计函数的执行时间
# 输出日志
import time


def decorator(func):
    def inner():
        # 内部函数对已有函数进行装饰
        # 获取当前时间 time.time() 得到的值是相对于 1970-1-1 0:0:1 的时间差
        start = time.time()
        func()
        end = time.time()
        print("函数执行的时间：", end-start)
    return inner


@decorator
def work():
    for i in range(10000):
        print(i)


work()

