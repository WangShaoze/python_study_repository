
# 自定义上下文管理器的实现  __enter__ 和 __exit__
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("over")
        self.file.close()


with File("yi.txt", "r") as f:
    # print(f.read())
    f.write("fjdslkaj")
