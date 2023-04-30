# 外部函数 接受姓名参数
def config_name(name):

    def inner(msg):
        print(name+":"+msg)
    # 外部函数保存内部函数的参数，并且完成数据现实的组成

    print(id(inner))
    # 外部函数返回内部函数
    return inner


# 创建闭包实例
tom = config_name("tom")
jerry = config_name("jerry")

tom("哥们，出来玩一下")
jerry("打死都不出去。")
tom("我不吃你")
jerry("我信你个鬼")
