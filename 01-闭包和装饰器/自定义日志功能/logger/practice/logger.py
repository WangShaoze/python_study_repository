import time
import inspect
import sys
import os

log_output: type


class Color:
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    RESET = "\033[0m"  # 结束值


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


log: Log  # 类或者方法


class Logger:
    fo = None
    stdout = sys.stdout

    def __init__(self, time_format: str = "%Y-%m-%d %H:%M:%S"):
        self.time_format = time_format
        self.func = None

    def set_fo(self, log_path_dir):
        if self.fo is None:
            if os.path.exists(log_path_dir):
                if os.path.isdir(log_path_dir):
                    self.fo = open("{}/{}_app.log".format(log_path_dir, time.strftime("%Y%m%d-%H%M%S")), mode="a+",
                                   encoding="utf-8")
                else:
                    raise "log_path_dir should be a directory"
            else:
                raise "log_path_dir not exist"
        return self

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
            print("{}[{}] function:[{}] {} [{}]{}".format(color, time.strftime(self.time_format), caller, log_level,
                                                          message.format(*args, **kwargs), Color.RESET))
        else:
            print("{}[{}] function:[{}] {} [{}]{}".format(color, time.strftime(self.time_format), caller, log_level,
                                                          message, Color.RESET))

    def inner(self, *args, **kwargs):
        global log, log_output
        fg = inspect.currentframe().f_back.f_globals  # 栈帧的操作 ===> 获取到执行 test 的模块
        try:
            if not fg.get("log"):
                log = Log
                fg["log"] = log
            log_output = self._log
            rsl = self.func(*args, **kwargs)
            return rsl
        except Exception as e:
            log.critical("函数执行出错...")
            raise e
        finally:
            pass

    def __call__(self, func: type):
        self.func = func
        return self.inner

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


def log_path(log_path_dir: str):
    def outer(func: type):
        def inner(*args, **kwargs):
            sys.stdout = Logger().set_fo(log_path_dir)
            rsl = func(*args, **kwargs)
            sys.stdout = sys.__stdout__
            return rsl

        return inner

    return outer


LogPath = log_path


def log_config(func: type):
    _log_path = None

    def get_log_path():
        nonlocal _log_path
        with open("./log_config.cnf", "r", encoding="utf-8") as f:
            d = f.read()
            for u in d.split("[**>]"):
                if "log_path:" in u.strip("[**]"):
                    _log_path = u.split("log_path:")[1]
                    break
            else:
                raise "log_path not exist"

    def inner(*args, **kwargs):
        if _log_path:
            sys.stdout = Logger().set_fo(_log_path)
            rsl = func(*args, **kwargs)
            sys.stdout = sys.__stdout__
        else:
            raise "log_path not exist, decorate not succeed"
        return rsl

    if not _log_path:
        get_log_path()
    return inner


LogConfig = log_config

# @Logger(
#     "%Y-%m-%d %H:%M:%S")  # logger = Logger()  ==> @logger ==> inner = logger(test) ===> test = inner ===> test(name)
# def test(name: str):
#     log.info("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#
#
# @Logger(
#     "%Y-%m-%d %H:%M:%S")  # logger = Logger()  ==> @logger ==> inner = logger(test) ===> test = inner ===> test(name)
# @LogPath("./")
# def test2(name: str):
#     log.info("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#     log.debug("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#     log.warning("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#     log.error("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#     log.critical("我是{}, 我今年{}岁, 毕业于{}", name, 23, "四川大学")
#

# if __name__ == "__main__":
#     test("胡歌")
#     test2("刘涛")
