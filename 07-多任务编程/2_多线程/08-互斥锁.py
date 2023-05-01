import threading

g_num = 0
# 设置互斥锁，Lock本质上是一个函数，通过调用函数，创建互斥锁
lock = threading.Lock()


# 定义一个任务遍历100000
def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 这里需要将g_num声明全局变量，应为内存地址在累加的过程中已经改变
        global g_num
        g_num = g_num + 1
    # 代码到处循环结束
    print('遍历100000,task1结束：', g_num)
    # 释放锁
    lock.release()


def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 这里需要将g_num声明全局变量，应为内存地址在累加的过程中已经改变
        global g_num
        g_num = g_num + 1
    # 代码到处循环结束
    print('遍历100000结束，task2结束：', g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    first_threading = threading.Thread(target=task1)
    second_threading = threading.Thread(target=task2)

    first_threading.start()
    # 为了避免出现错误，为线程设置互斥锁，等第一个线程执行完成后，在执行第二个线程
    second_threading.start()

'''
结论：互斥锁可以保证同一时刻只有一个线程执行代码，可以保证线程执行代码不会出错
     线程等待和互斥锁都是将原来的多个线程改为单线程，可以保证数据的正确性，但是执行的效率降低了
'''
