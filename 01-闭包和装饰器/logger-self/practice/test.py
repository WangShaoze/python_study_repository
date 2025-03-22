from logger import *


def hello():
    log.info('hello')


def test(n, m):
    hello()
    log.info("m={},n={}", m, n)
    return n * m


def test1(x, y, z):
    log.info("init ==>[x={}, y={}, z={}]".format(x, y, z))
    for i in range(x, z):
        if i % 6 == 0:
            log.warning(str(i))
        log.debug("i={}, y={}, i+y={}".format(i, y, i + y))
    return x + y + z


def test2(x, y):
    try:
        for _ in range(10):
            rsl = x / y
            if y < 0:
                log.warning("y is less than zero and rsl is {}", rsl)
            else:
                log.info(rsl)
            y -= 1
    except ZeroDivisionError:
        log.error("Division by zero")
        log.critical("出错了， 0 不可以作为除数!")


# @Logger("./log_config.cnf", "%Y-%m-%d-%H:%M:%S", "test_app.log")
@Logger("./log_config.cnf", time_formate="%Y-%m-%d-%H:%M:%S", log_filename="test_app.log")
@LogStart
def main():
    log.info("开始执行test函数...")
    print(test(4, 5))
    log.info("开始执行test1函数...")
    test1(10, 3, 101)
    log.info("开始执行test2函数...")
    test2(100, 18)
    log.info("执行结束...")


if __name__ == '__main__':
    main()
