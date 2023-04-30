# 类装饰器：用类装饰已有函数
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func
        pass

    # __call__ : 可以实现让对象变成可调用的对象，可调用的对象可以像函数一样使用
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print("课已经讲完。")
        self.__func()


@MyDecorator  # @MyDecorator =====> show=MyDecorator(show)
def show():
    print("快要放学了。")


# 执行show   # 执行 MyDecorator类创建实例对象-----------> show()  ====> 对象
show()  # 该函数之所以能够调用，是因为__call__的使用
