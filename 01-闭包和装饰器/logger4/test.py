from logger import *


@Log
def test2():
    log.info("你好")


@Log  # @Log ==> log = Log(test1)  ==> test1 = log  ==> test1(params) <==> log(params)
def test1():
    log.info("fdsfd")
    test2()


# @Logger(log_config="./log_config.cnf")
@Logger("./log_config.cnf")
# @Logger(time_formate="%Y-%m-%d-%H:%M:%S", log_filename="./output.log")
@LogStart  # inner = log_start(test)   ==> test = inner ==> test(params)  <==> inner(params)
@Log
def test(n):
    test1()
    log.info("你好，这是test函数...")
    log.debug("n:{}", n)
    log.warn("n:{}", n)
    log.error("n:{}", n)
    log.critical("n:{}", n)


if __name__ == '__main__':
    test(12)  # 装饰过以后，其实真正调用了 wrapper
