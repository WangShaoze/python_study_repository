import multiprocessing
import time


def task():

    while True:
        for i in range(10):
            print("打印：", i)
            time.sleep(0.5)
            print('程序执行中...')


if __name__ == '__main__':
    # 创建子进程
    sub_processing = multiprocessing.Process(target=task)

    # #将子进程设置为守护主进程
    # sub_processing.daemon = True
    sub_processing.start()

    # 主进程延时1秒钟
    time.sleep(1)
    # 让子进程在主进程退出之前就销毁
    sub_processing.terminate()
    print('over！')


# 结论：主进程会等待所有子进程执行完成后在结束

# 如果子进程一直不结束，主进程也不会结束----解决办法---让主进程推出前销毁子进程
# 1.将子进程设置为守护主进程，主进程推出子进程销毁，这样子进程会依赖主进程
# 2.让子进程在主进程推出之前就销毁
