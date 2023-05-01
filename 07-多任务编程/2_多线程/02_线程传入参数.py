import threading


def show_info(name, age):
    print('你的名字是%s是，年龄是%d' % (name, age))


if __name__ == '__main__':

    # 创建子线程,以元组的方式传入参数
    # sub_info = threading.Thread(target=show_info, args=('小李', 45))

    # 创建子线程,以字典的方式传入参数
    sub_info = threading.Thread(target=show_info, kwargs={'name': '王小五', 'age': 23})

    # 创建子线程, 混合传参
    show_info = threading.Thread(target=show_info, args=('xiao_wan',), kwargs={'age': 12})

    # 启动子线程
    sub_info.start()
