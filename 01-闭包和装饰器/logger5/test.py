from logger import *

@Log   # 只有被被这个装饰器修饰的函数才可以使用log.xxx，否则直接报错
def test1():
    log.info("this is test1 ")
    log.error("this is test1 ")


# logger = Logger(time_format="%Y-%m-%d-%H:%M:%S") ==> wrapper = logger(test) ==> test = wrapper ==> test(10)
#@Logger(time_format="%Y-%m-%d-%H:%M:%S", log_filename="/home/wangshaoze/desktop/output_log.log")   # 这里传入的都是配置项
#@Logger(log_config="log_config.cnf", time_format="%Y-%m-%d-%H:%M:%S", log_filename="/home/wangshaoze/desktop/output_log.log")   # 这里传入的都是配置项
@Logger("log_config.cnf", time_format="%Y-%m-%d-%H:%M:%S", log_filename="/home/wangshaoze/desktop/output_log.log")   # 这里传入的都是配置项
@LogStart
@Log
def test(n):  # 使用一个带参数的类装饰器来装饰这个函数
    n += 10
    log.debug("n={}".format(n))
    log.info("n={}".format(n))
    log.warn("n={}".format(n))
    log.error("n={}".format(n))
    log.critical("n={}".format(n))
    return n


if __name__ == "__main__":
    rsl = test(10)
    print("test 函数执行的结果:{}".format(rsl))
    test1()
