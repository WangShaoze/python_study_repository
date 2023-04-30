from contextlib import contextmanager


@contextmanager
def my_open(file_name, file_mode):
    try:

        file = open(file_name, file_mode)
        yield file  # yeild 上面的代码认为时 上文的代码,下面的代码默认是 下文的代码
    except Exception as e:
        print(e)
    finally:
        print("over")
        file.close()


# TypeError: 'generator' object does not support the context manager protocol
# with 语句需要结合上下文管理器,普通的方法,不可以
with my_open(file_name="yi.txt", file_mode="r") as f:
    # data = f.read()
    # print(data)

    f.write("hfjakhkdsa")
