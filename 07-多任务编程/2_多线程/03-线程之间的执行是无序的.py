import threading
import time


def show_text():
    time.sleep(0.5)
    # 获取当前线程
    print(threading.current_thread())


if __name__ == '__main__':
    # 循环创建大量线程，测试线程之间的无序性
    for i in range(30):
        # 创建子线程
        sub_threading = threading.Thread(target=show_text, name=f'sub_thread{i}')
        # 启动子线程
        sub_threading.start()

'''结论：子线程执行是无序的'''
