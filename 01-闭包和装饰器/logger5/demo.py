import inspect

def test1():
    caller = inspect.stack()[1]
    caller_name = caller.function
    caller_frame = inspect.currentframe().f_back
    call_line = caller_frame.f_lineno
    print("this is func test1  and test1 is called by {} , is called in {} line...".format(caller_name, call_line))


def test():
    test1()
    print("this is func test and test1 is called by test ...")

if __name__ == "__main__":
    test()
