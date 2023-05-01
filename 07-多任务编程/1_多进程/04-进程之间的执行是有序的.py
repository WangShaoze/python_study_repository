import multiprocessing
import time


def show_text():
    time.sleep(0.5)
    # 获取当前进程
    print(multiprocessing.current_process())


if __name__ == '__main__':
    # 循环创建大量进程，测试进程执行的无序性
    for i in range(30):
        # 创建子进程
        sub_multiprocessing = multiprocessing.Process(target=show_text, name=f'sub_multiprocessing{i}')
        # 启动子进程
        sub_multiprocessing.start()

'''结论：子进程执行是无序的'''
