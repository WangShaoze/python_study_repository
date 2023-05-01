import threading
import time


def task():
    while True:
        print("子线程执行中...")
        time.sleep(0.1)


if __name__ == '__main__':

    # daemon=True 表示创建子线程守护主线程，主线程退出子线程直接销毁
    sub_threading = threading.Thread(target=task,daemon=True)
    sub_threading.start()

    # 主线程的结束时间
    time.sleep(3)
    print('over.')
    # exit()

'''
结论：主线程会等待子线程结束后在结束
解决办法:把主线程设置为守护子线程
'''