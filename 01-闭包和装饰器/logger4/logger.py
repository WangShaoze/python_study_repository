"""
目标是是做一个日志模块:
    1.争取在一个模块中实现
    2.可以显示每条日志的执行时间，执行函数，行号，日志级别，日志内容
        time  ==> "%Y%m%d-%H%M%S" / "%Y-%m-%d-%H:%M:%S"
        inspect ==> caller = inspect.stack()[1] ==> caller_name = caller.function
                ==> caller_frame = inspect.currentframe().f_back ==> caller_frame.f_lineno
    3.日志需要写入单独的文件中，保证在开发环境及生产环境都可以看到日志 （需要保证单例及路径配置）
    4.多线程环境下可以使用（线程安全）
    5.调试时日志级别不同可以显示不同的颜色
        class Color:
            BLUE = '\033[94m'
            WHITE = '\033[97m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            PURPLE = '\033[95m'
            RESET = "\033[0m"  # 结束值



    如果由相关的业务需要，可以直接 +V   ==>  WSZ18313632768
"""
import sys
import threading
import time
import inspect

log_output: type


class Color:
    BLUE = '\033[94m'  # DEBUG
    WHITE = '\033[97m'  # INFO
    YELLOW = '\033[93m'  # WARN
    RED = '\033[91m'  # ERROR
    PURPLE = '\033[95m'  # CRITICAL
    RESET = "\033[0m"  # 结束值


funcs = []


class Log:
    def __init__(self, func: type):
        global funcs
        funcs.append(func.__name__)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def debug(msg: str, *args, **kwargs) -> None:
        caller = inspect.stack()[1]  # 获取调用函数是谁
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno
        color = Color.BLUE  # INFO
        log_output(msg, caller_name, caller_line, color, "DEBUG", *args, **kwargs)

    @staticmethod
    def info(msg: str, *args, **kwargs) -> None:
        caller = inspect.stack()[1]  # 获取调用函数是谁
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno
        color = Color.WHITE  # INFO
        log_output(msg, caller_name, caller_line, color, "INFO", *args, **kwargs)

    @staticmethod
    def warn(msg: str, *args, **kwargs) -> None:
        caller = inspect.stack()[1]  # 获取调用函数是谁
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno
        color = Color.YELLOW
        log_output(msg, caller_name, caller_line, color, "WARN", *args, **kwargs)

    @staticmethod
    def error(msg: str, *args, **kwargs) -> None:
        caller = inspect.stack()[1]  # 获取调用函数是谁
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno
        color = Color.RED
        log_output(msg, caller_name, caller_line, color, "ERROR", *args, **kwargs)

    @staticmethod
    def critical(msg: str, *args, **kwargs) -> None:
        caller = inspect.stack()[1]  # 获取调用函数是谁
        caller_name = caller.function
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno
        color = Color.PURPLE
        log_output(msg, caller_name, caller_line, color, "CRITICAL", *args, **kwargs)


log: Log


class Logger:
    _instance = None

    lock = threading.Lock()  # 构造一把所，保证在多线程的环境下运行，这个Logger仍然时单例的

    sys_stdout = sys.stdout

    fo = None
    log_filename = None

    log_config = None
    flag = True

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.func = None
        if len(args) != 0:
            self.log_config = args[0]
        if "log_config" in kwargs:
            self.log_config = kwargs["log_config"]
        if "time_formate" in kwargs:
            self.time_formate = kwargs["time_formate"]
        if "log_filename" in kwargs:
            self.log_filename = kwargs["log_filename"]
        if self.log_config and self.flag:
            self.load_log_config()

    def load_log_config(self):
        with open(self.log_config, mode="r", encoding="utf-8") as fi:
            configs = {uni[0]: uni[1] for uni in
                       [u.strip("\n").strip().strip("[**]").strip("[**>]").split("[*-*]") for u in
                        fi.read().split("[**>]") if u != '']}
            if "time_formate" in configs:
                self.time_formate = configs["time_formate"]
            if "log_filename" in configs:
                self.log_filename = configs["log_filename"]
        if self.time_formate:
            self.time_formate = "%Y-%m-%d %H:%M:%S"
        self.flag = False

    def set_log_fo(self):
        if not self.fo and self.log_filename:
            self.fo = open(self.log_filename, mode="a+", encoding="utf-8")
        return self

    def _log_output(self, val, caller_name, caller_line, color, log_leval, *args, **kwargs):
        global funcs
        if caller_name not in funcs:
            raise Exception("非法使用log.xxx 请用@Log注解！")
        if len(args) != 0 or len(kwargs) != 0:
            print("{}[{}] FUNC:[{}], LINE:[{}] {} [{}]{}".format(color, time.strftime(self.time_formate), caller_name,
                                                                 caller_line,
                                                                 log_leval, val.format(*args, **kwargs), Color.RESET))
        else:
            print("{}[{}] FUNC:[{}], LINE:[{}] {} [{}]{}".format(color, time.strftime(self.time_formate), caller_name,
                                                                 caller_line,
                                                                 log_leval, val, Color.RESET))

    def wrapper(self, *args, **kwargs):
        global log_output, funcs
        log_output = self._log_output
        # 获取到调用Wrapper的模块
        cf = inspect.currentframe()
        fg = cf.f_back.f_globals  # 从栈帧中获取到调用wrapper的模块的全局变量
        if not fg.get("log"):
            fg["log"] = Log

        self.func(*args, **kwargs)

    def __call__(self, func: type):
        self.func = func
        return self.wrapper

    @staticmethod
    def replace(text: str):
        return text.replace(Color.WHITE, "") \
            .replace(Color.BLUE, "") \
            .replace(Color.RED, "") \
            .replace(Color.YELLOW, "") \
            .replace(Color.PURPLE, "") \
            .replace(Color.RESET, "")

    def write(self, text: str):
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


def log_start(func: type):
    def inner(*args, **kwargs):
        sys.stdout = Logger().set_log_fo()
        rsl = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return rsl

    return inner


LogStart = log_start
