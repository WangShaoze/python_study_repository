from logger import *

@Log
def test1(n):
    log.debug("N=10*n, n is {}, N is {}", n, 10*n)
    log.info("N=10*n, n is {}, N is {}", n, 10*n)
    log.warn("N=10*n, n is {}, N is {}", n, 10*n)
    log.error("N=10*n, n is {}, N is {}", n, 10*n)
    log.critical("N=10*n, n is {}, N is {}", n, 10*n)
    return 10*n

@LogStart
@Log
def test2(n):
    log.debug("N=10*n, n is {}, N is {}", n, 10*n)
    log.info("N=10*n, n is {}, N is {}", n, 10*n)
    log.warn("N=10*n, n is {}, N is {}", n, 10*n)
    log.error("N=10*n, n is {}, N is {}", n, 10*n)
    log.critical("N=10*n, n is {}, N is {}", n, 10*n)
    return 10*n

@Logger("./log_config.cnf", time_format="%Y-%m-%d-%H:%M:%S", log_filename="/home/wangshaoze/desktop/output_log.log")  #  logger = Logger(time_format="%Y-%m-%d-%H:%M:%S") ==> @logger ==> wrapper = logger(test)  ==> test = wrapper  ====> 等待 test(n)  执行
@LogStart
@Log   # 只有带有这个装饰器的函数才可以使用log.xxx的方法,我们应该如何去实现呢？# log = Log(test)  ==>  test = log  ====> 等待某一个时刻 test函数执行，就会触发 log(n) ==> __call__(n)
def test(n):
    test1(3)
    log.debug("N=10*n, n is {}, N is {}", n, 10*n)
    log.info("N=10*n, n is {}, N is {}", n, 10*n)
    log.warn("N=10*n, n is {}, N is {}", n, 10*n)
    log.error("N=10*n, n is {}, N is {}", n, 10*n)
    log.critical("N=10*n, n is {}, N is {}", n, 10*n)
    return 10*n

if __name__ == "__main__":
    rsl = test(9)
    print("test for 9 rsl is {}".format(rsl))
    test2(5)
    test2(6)
