import threading

g_num = 0
# 定义一个任务遍历100000


def task1():
    for i in range(1000000):
        # 这里需要将g_num声明全局变量，应为内存地址在累加的过程中已经改变
        global g_num
        g_num = g_num + 1
    # 代码到处循环结束
    print('遍历100000结束,task1结束：', g_num)


def task2():
    for i in range(1000000):
        # 这里需要将g_num声明全局变量，应为内存地址在累加的过程中已经改变
        global g_num
        g_num = g_num + 1
    # 代码到处循环结束
    print('遍历100000结束，task2结束：', g_num)


if __name__ == '__main__':

    first_threading = threading.Thread(target=task1)
    second_threading = threading.Thread(target=task2)

    first_threading.start()
    # 为了避免出现错误，必须设置线程等待，等第一个线程执行完成后，在执行第二个线程
    first_threading.join()  # 这里是主线程等待第一个子线程执行完成后，再往下执行第二个线程
    second_threading.start()
