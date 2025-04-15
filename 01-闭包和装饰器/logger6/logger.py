import os
import sys
import time
import inspect
import threading


"""
需要实现的目标是:
    1.输出日志，格式: 日志输出的时间，执行函数，在该模块中的行号，日志级别，具体的日志内容
    2.调试环境中，不同日志级别显示出不同的颜色
    3.需要将日志写入到一个文件中去，要求和调试环境中的日志内容完全一致，颜色不用
    4.需要实现安全的日志配置
"""
class Color:
    """
    用于控制某一个日志级别的颜色，
    利用print函数输出信息的时候的颜色控制方法,
    RESET 是只该颜色涂刷的结束位置
    """
    BLUE = '\033[94m'  # DEBUG
    WHITE = '\033[97m' # INFO
    YELLOW = '\033[93m' # WARN
    RED = '\033[91m'   # ERROR 
    PURPLE = '\033[95m' # CRITICAL
    RESET = "\033[0m"  # 结束值

log:type
log_output:type

funcs = []

class Log:
    def __init__(self, func:type):
        global funcs
        self.func = func
        funcs.append(func.__name__)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def judge(caller):
        global funcs
        if caller not in funcs:
            raise Exception("the usage is not illegal, you should use the decotor of [@Log], while you can use [log.xxx] !")


    @staticmethod
    def debug(val, *args, **kwargs):
        caller = inspect.stack()[1]  # 通过自省机制这个库，调用获取栈空间的方法，获取到第二个出栈的方法，即调用该函数的那个函数
        caller_name = caller.function  # 通过这个函数获取到这个函数的名称
        lineno = inspect.currentframe().f_back.f_lineno # 获取当前函数，正在被调用的位置所在的模块，并通过模块的栈空间，获取到调用位置所处的行
        log_leval, color = "DEBUG", Color.BLUE
        log_output(val,caller_name, lineno, log_leval,color, *args, **kwargs)

    @staticmethod
    def info(val, *args, **kwargs):
        caller = inspect.stack()[1]  # 通过自省机制这个库，调用获取栈空间的方法，获取到第二个出栈的方法，即调用该函数的那个函数
        caller_name = caller.function  # 通过这个函数获取到这个函数的名称
        lineno = inspect.currentframe().f_back.f_lineno # 获取当前函数，正在被调用的位置所在的模块，并通过模块的栈空间，获取到调用位置所处的行
        log_leval, color = "INFO", Color.WHITE
        log_output(val,caller_name, lineno, log_leval,color, *args, **kwargs)

    @staticmethod
    def warn(val, *args, **kwargs):
        caller = inspect.stack()[1]  # 通过自省机制这个库，调用获取栈空间的方法，获取到第二个出栈的方法，即调用该函数的那个函数
        caller_name = caller.function  # 通过这个函数获取到这个函数的名称
        lineno = inspect.currentframe().f_back.f_lineno # 获取当前函数，正在被调用的位置所在的模块，并通过模块的栈空间，获取到调用位置所处的行
        log_leval, color = "WARN", Color.YELLOW
        log_output(val,caller_name, lineno, log_leval,color, *args, **kwargs)

    @staticmethod
    def error(val, *args, **kwargs):
        caller = inspect.stack()[1]  # 通过自省机制这个库，调用获取栈空间的方法，获取到第二个出栈的方法，即调用该函数的那个函数
        caller_name = caller.function  # 通过这个函数获取到这个函数的名称
        lineno = inspect.currentframe().f_back.f_lineno # 获取当前函数，正在被调用的位置所在的模块，并通过模块的栈空间，获取到调用位置所处的行
        log_leval, color = "ERROR", Color.RED
        log_output(val,caller_name, lineno, log_leval,color, *args, **kwargs)

    @staticmethod
    def critical(val, *args, **kwargs):
        caller = inspect.stack()[1]  # 通过自省机制这个库，调用获取栈空间的方法，获取到第二个出栈的方法，即调用该函数的那个函数
        caller_name = caller.function  # 通过这个函数获取到这个函数的名称
        lineno = inspect.currentframe().f_back.f_lineno # 获取当前函数，正在被调用的位置所在的模块，并通过模块的栈空间，获取到调用位置所处的行
        log_leval, color = "CIRITCAL", Color.PURPLE
        log_output(val,caller_name, lineno, log_leval,color, *args, **kwargs)



class Logger:
    """
    步骤:
        1.实现一个简单的类装饰器功能，在test函数执行前后，打印处执行的时间,时间输出的格式需要按照 %Y-%m-%d-%H:%M:%S
        2.改造: 我们需要的不是在一个函数执行前或者后去输出日志，而是需要在函数内部去使用这个日志函数
        3.我们将测试的代码移动到另外的一个模块中去，出现问题了...,居然出现找不到log的错误,解决这个问题的关键在于Python中模块与模块之间的全局变量问题
        4.我们应该如何去控制日志级别的实现，以及每一个日志级别的颜色，如何控制...
        5.如果现在存在第二个函数test1，也使用了log.xxx相关函数，既然可以运行，这里是不是因为 Log 这个类被注入的时候是以全局变量的方式注入的，所以只要有一处注入了，同一个模块中都是可以使用的，所以需要控制log.xxx的使用权限
        6.如何将文件写入到文件中去，如何保证所做配置是单例性质，以及多线程环境下是否还能位置单例呢？
        7.如何做配置，现在这个日志，只有2个配置 time_format , log_filename, 假设还有更多的配置，我们应该更好的去做配置呢？
    """
    _instance = None
    lock = threading.Lock()  # 构造一把锁，只有获取到锁的时候才可以对实例进行操作
    sys_stdout = sys.stdout
    fo = None
    time_format="%Y-%m-%d-%H:%M:%S"
    log_filename="./output_log.log"
    first_config = True

    def __new__(cls, *args, **kwargs):
        with cls.lock:  # 自动获取和释放锁
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.func = None
        if len(args) != 0:
            self.log_config = args[0]
        if "log_config" in kwargs:
            self.log_config = kwargs["log_config"]
        if "time_format" in kwargs:
            self.time_format = kwargs["time_format"]
        if "log_filename" in kwargs:
            self.log_filename = kwargs["log_filename"]
        if self.first_config and self.log_config:
            self.load_log_config()
        self.set_log_fo()

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
                    self.time_format = configs["time_format"]
                if "log_filename" in configs:
                    self.log_filename = configs["log_filename"]
                self.first_config = False  # 只会成功做一次配置

    def set_log_fo(self):
        """
        if not os.path.isfile(self.log_filename):
            raise Exception("the path [{}] is not a file.".format(self.log_filename))
        """
        self.fo = open(self.log_filename, mode="a+", encoding="utf-8")
        return self

    def log_output(self, val, caller, lineno, log_leval,color, *args, **kwargs):
        Log.judge(caller)
        if len(args) != 0 or len(kwargs) != 0:
            print("{}[{}] FUNC:[{}] LINE:[{}] [{}] [{}]{}".format(color, time.strftime(self.time_format), caller, lineno, log_leval, val.format(*args, **kwargs), Color.RESET))
        else:
            print("{}[{}] FUNC:[{}] LINE:[{}] [{}] [{}]{}".format(color, time.strftime(self.time_format), caller, lineno, log_leval, val, Color.RESET))

    def wrapper(self, *args, **kwargs):
        # self.log_output("this is test start ...")
        global log_output
        log_output = self.log_output
        cf = inspect.currentframe()  # 获取正在调用wrapper的模块
        fb = cf.f_back  # 获取栈空间
        fg = fb.f_globals  # 获取全局变量,全局变量是被封装在一个字典中的，所以其本质就是一个字典
        if not fg.get("log"):
            # fg["log"] = self.log_output
            fg["log"] = Log
        rsl = self.func(*args, **kwargs)
        # self.log_output("this is test end ...")
        return rsl

    def __call__(self, func:type):
        self.func = func
        return self.wrapper

    @staticmethod
    def replace(text:str):
        return text.replace(Color.RESET, "")\
            .replace(Color.BLUE, "")\
            .replace(Color.WHITE, "")\
            .replace(Color.YELLOW, "")\
            .replace(Color.RED, "")\
            .replace(Color.PURPLE, "")

    def write(self, text:str):
        self.sys_stdout.write(text)
        if self.fo:
            self.fo.write(self.replace(text))

    def flush(self):
        self.sys_stdout.flush()
        if self.fo:
            self.fo.flush()

    def __del__(self):
        if self.fo:
            self.fo.close()
        self.fo

def log_start(func:type):
    def inner(*args, **kwargs):
        sys.stdout = Logger().set_log_fo()
        rsl = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return rsl
    return inner

LogStart = log_start

