import threading
import time

# 定义全局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(10):
        g_list.append(i)
        print("现在正在添加：", i)
        # time.sleep(0.2)
    # 数据到此处已经添加完成了
    print('添加数据完成了。', g_list)


# 读取数据的任务
def read_data():
    print('读取到的数据为：', g_list)


if __name__ == '__main__':

    # 添加线程和读取线程
    add_threading = threading.Thread(target=add_data)
    read_threading = threading.Thread(target=read_data)

    # 开始两个线程
    add_threading.start()
    # time.sleep(6)

    # 让当前线程（主线程）等待子线运行结束之后再往下继续执行代码
    add_threading.join()
    read_threading.start()

'''结论：线程之间可以共享全局变量'''
