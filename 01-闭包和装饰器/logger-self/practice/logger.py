import os
import sys
import time
import inspect
import threading


class Color:
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    RESET = "\033[0m"  # 结束值


log_output: type


class Log:
    @classmethod
    def debug(cls, message: str, *args, **kwargs):
        caller = inspect.stack()[1]  # 获取到当前执行该函数的那个函数
        caller_name = caller.function
        log_output(caller_name, "DEBUG", message, *args, **kwargs)

    @classmethod
    def info(cls, message: str, *args, **kwargs):
        caller = inspect.stack()[1]  # 获取到当前执行该函数的那个函数
        caller_name = caller.function
        log_output(caller_name, "INFO", message, *args, **kwargs)

    @classmethod
    def warning(cls, message: str, *args, **kwargs):
        caller = inspect.stack()[1]  # 获取到当前执行该函数的那个函数
        caller_name = caller.function
        log_output(caller_name, "WARN", message, *args, **kwargs)

    @classmethod
    def error(cls, message: str, *args, **kwargs):
        caller = inspect.stack()[1]  # 获取到当前执行该函数的那个函数
        caller_name = caller.function
        log_output(caller_name, "ERROR", message, *args, **kwargs)

    @classmethod
    def critical(cls, message: str, *args, **kwargs):
        caller = inspect.stack()[1]  # 获取到当前执行该函数的那个函数
        caller_name = caller.function
        log_output(caller_name, "CRITICAL", message, *args, **kwargs)


log: Log


class Logger:
    _instance = None
    _lock = threading.Lock()
    fo = None
    stdout = sys.stdout

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_path: str = None, *args, **kwargs):
        self.time_formate = "%Y%m%d %H%M%S"
        self.log_filename = None
        self.func = None
        try:
            if args:
                self.time_formate = args[0]
            if "time_formate" in kwargs:
                self.time_formate = kwargs["time_formate"]
            if args and len(args) == 2:
                self.log_filename = args[1]
            if "log_filename" in kwargs:
                self.log_filename = kwargs["log_filename"]
            if config_path:
                log_path = self.get_log_path(config_path)
                self.set_fo(log_path)
        except Exception as e:
            print(e)

    def set_fo(self, log_path_dir):
        if not self.fo and os.path.exists(log_path_dir) and os.path.isdir(log_path_dir):
            log_file_path = os.path.join(log_path_dir,
                                         "{}_{}".format(time.strftime("%Y%m%d-%H%M%S"), self.log_filename))
            self.fo = open(log_file_path, mode="a+", encoding="utf-8")

    def set_time_formate(self, time_formate):
        self.time_formate = time_formate

    def _log(self, caller, log_level, message: str, *args, **kwargs):
        color = Color.WHITE
        if log_level == "DEBUG":
            color = Color.BLUE
        if log_level == "INFO":
            color = Color.WHITE
        if log_level == "WARN":
            color = Color.YELLOW
        if log_level == "ERROR":
            color = Color.RED
        if log_level == "CRITICAL":
            color = Color.PURPLE
        if len(args) > 0 or len(kwargs) > 0:
            print("{}[{}] function:[{}] {} [{}]{}".format(color, time.strftime(self.time_formate), caller, log_level,
                                                          message.format(*args, **kwargs), Color.RESET))
        else:
            print("{}[{}] function:[{}] {} [{}]{}".format(color, time.strftime(self.time_formate), caller, log_level,
                                                          message, Color.RESET))

    @staticmethod
    def get_log_path(log_config_path):
        with open(log_config_path, "r", encoding="utf-8") as f:
            d = f.read()
            for u in d.split("[**>]"):
                if "log_path:" in u.strip("[**]"):
                    return u.split("log_path:")[1]
            else:
                raise "log_path not exist"

    def wrapper(self, *args, **kwargs):
        func = self.func
        global log, log_output
        fg = inspect.currentframe().f_back.f_globals  # 栈帧的操作 ===> 获取到执行 test 的模块
        try:
            if not fg.get("log"):
                log = Log
                fg["log"] = log
            log_output = self._log
            rsl = func(*args, **kwargs)
            return rsl
        except Exception as e:
            log.critical("函数执行出错...")
            raise e
        finally:
            pass

    def __call__(self, func):
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

    def write(self, text):
        self.stdout.write(text)
        if self.fo:
            self.fo.write(self.replace(text))

    def flush(self):
        # 刷新终端输出;f
        self.stdout.flush()
        if self.fo:
            # 刷新文件输出
            self.fo.flush()

    def __del__(self):
        if self.fo:
            self.fo.close()


def log_start(func: type):
    def inner(*args, **kwargs):
        sys.stdout = Logger()
        rsl = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return rsl

    return inner


LogStart = log_start

if __name__ == "__main__":
    def example_function():
        log.info("Inside the function")


    @Logger(config_path="./log_config.cnf", time_formate="%Y-%m-%d-%H:%M:%S")
    @LogStart
    def main():
        log.info("Inside the function")
        example_function()
        log.info("Inside the function")


    main()
