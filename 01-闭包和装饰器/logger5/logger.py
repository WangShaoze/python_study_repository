import sys
import time
import inspect
import threading
"""
我们实现日志模块的目标是:
    1.每一条日志可以显示: 日志的执行时间，执行函数，行号，日志级别，日志内容
    2.再调试环境下，更具日志级别显示不同的颜色
    3.保证配置只会做一次
    4.需要将日志输出到一个文件中去

inspect  这个模块是Python中用于做反射使用的，也是就实现python中做自省机制的模块
我们要用它来做什么？
1. 做全局变量的投射，刚刚在test函数中，不能成功的访问log函数，那么我们就可以使用这个库把log函数投射到test模块的全局变量中
2. 获取执行该函数的函数是谁？
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno

为了实现在多线程环境下依然可以安全的访问，那么需要实现线程安全的单例配置

为例实现将日志输出到文件中，我们需要重定向的将print输出的文字，写入到文件中去

为了可以将Logger的配置项，通过文件的形式传递，就需要将配置项以某种格式写入到配置文件中，在加载出来这个配置,而且匹配文件中的配置项，优先级最高
"""



class Color:
    BLUE = '\033[94m'  # DEBUG
    WHITE = '\033[97m' # INFO
    YELLOW = '\033[93m' # WARN
    RED = '\033[91m'   # ERROR 
    PURPLE = '\033[95m' # CRITICAL
    RESET = "\033[0m"  # 结束值


log_output:type

funcs = []

class Log:
    """ 这里实现装饰器是为了控制日志的访问权限  """
    def __init__(self, func:type):
        global funcs
        funcs.append(func.__name__)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


    @staticmethod
    def debug(val):
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno
        log_output(val,"DEBUG", Color.BLUE, caller_name, call_line)

    @staticmethod
    def info(val):
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno
        log_output(val,"INFO", Color.WHITE, caller_name, call_line)

    @staticmethod
    def warn(val):
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno
        log_output(val,"WARN", Color.YELLOW, caller_name, call_line)

    @staticmethod
    def error(val):
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno
        log_output(val,"ERROR", Color.RED, caller_name, call_line)

    @staticmethod
    def critical(val):
        caller = inspect.stack()[1]
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        call_line = caller_frame.f_lineno
        log_output(val,"CRITICAL", Color.PURPLE, caller_name, call_line)


log:Log

class Logger:
    """ 使用这个类来做配置 """
    _instance = None
    _lock = threading.Lock()   # 这里在做配置的时候需要获取一把锁，这可以保证在多线程的环境下，这个配置依然是单例的

    # 如果需要将print输出的日志，输出到一个文件中去，那么需要重构sys的输出流,还需要构建一个文件流
    sys_stdout = sys.stdout
    fo = None
    log_config = None
    first_config = True

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self,*args, **kwargs):
        if len(args) != 0:
            self.log_config = args[0]
        if "log_config" in kwargs:
            self.log_config = kwargs["log_config"]
        if "time_format" in kwargs:
            self.__time_format = kwargs["time_format"]
        if "log_filename" in kwargs:
            self.log_filename = kwargs["log_filename"]
        if self.log_config and self.first_config:
            self.load_log_config()
        if self.__time_format == "" or self.__time_format is None:
            self.__time_format = "%Y-%m-%d-%H:%M:%S"
        if self.log_filename == "" or self.log_filename is None:
            self.log_filename = "./output_log.log"


    def load_log_config(self):
        with open(self.log_config, mode="r", encoding="utf-8") as fi:
            config_content = fi.read()
            config_content = config_content.strip().strip("\n")
            if config_content:
                configs = {}
                for u in config_content.split("[**>]"):
                    u = u.strip().strip("\n").strip("[**]").strip("[**>]")
                    if u != "" and u is not None:
                        u_li = u.split("[*-*]")
                        configs[u_li[0]] = u_li[1]


                if "time_format" in configs:
                    self.__time_format = configs["time_format"]
                if "log_filename" in configs:
                    self.log_filename = configs["log_filename"]
                self.first_config = False  # 只会成功做一次配置






    def log_output(self, val, log_leval, color, caller_name, call_line):
        global funcs
        if caller_name not in funcs:
            raise Exception("非法使用 log.xxx 请使用注解 @Log 装饰")
        print("{}[{}] [{}] FUNC:[{}] LINE:[{}] [{}]{}".format(color, time.strftime(self.__time_format),log_leval, caller_name, call_line, val, Color.RESET))

    def wrapper(self, *args, **kwargs):
        global log_output   # 这里需要重点注意，这里声明的 log_output 全局变量只能在当前模块下使用，不能被引入到其他模块中
        log_output = self.log_output
        # 获取正在使用wrapper函数的模块
        cf = inspect.currentframe()
        # 获取该模块的全局变量
        fg = cf.f_back.f_globals  # 这个全局变量本质是一个字典，f_back 是什么？ f_back 是cf的栈，我们我们可以从栈中获取到这个模块的全局变量
        if not fg.get("log"):
            fg["log"] = Log
        # self.log_output("func start ...")
        rsl = self.__func(*args, **kwargs)
        # self.log_output("func end ...")
        return rsl

    def __call__(self, target):
        self.__func = target
        return self.wrapper

    def set_log_fo(self):
        if not self.fo and self.log_filename:
            self.fo =  open(self.log_filename, mode="a+", encoding="utf-8")
        return self

    @staticmethod
    def replace(text:str):
        return text.replace(Color.RESET, "")\
            .replace(Color.BLUE, "")\
            .replace(Color.WHITE, "")\
            .replace(Color.YELLOW, "")\
            .replace(Color.PURPLE, "")\
            .replace(Color.RED, "")

    def write(self, text):
        self.sys_stdout.write(text)
        if self.fo:
            self.fo.write(self.replace(text))

    def flush(self):
        self.sys_stdout.flush()
        if self.fo:
            self.fo.flush()

    def __del__(self):
        """当该配置对象被销毁的时候需要关闭文件流"""
        if self.fo:
            self.fo.close()


def log_start(target:type):
    def inner(*args, **kwargs):
        # 构建标准输出流
        sys.stdout = Logger().set_log_fo()
        rsl = target(*args, **kwargs)
        # 恢复标准输出流
        sys.stdout = sys.__stdout__
        return rsl
    return inner

LogStart = log_start
