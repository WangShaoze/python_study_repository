import multiprocessing
import time


# 定义 task 函数
def task():
    while True:
        for i in range(10):
            print('打印：', i)
            print('任务执行中....')
            time.sleep(0.9)
        print('程序执行之中。。。')


# 创建子进程
sub_process = multiprocessing.Process(target=task)

if __name__ == '__main__':
    # 启动子进程
    # # 设置子进程为守护主进程
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(3)
    # 在主进程推出之前， 让子进程先销毁
    sub_process.terminate()
    print('over！')  # 代码执行到这里 --- 并没有结束---继续执行子程序的代码

'''结论：
主程序 会等待子程序运行结束之后---在结束

解决办法：主进程退出子进程销毁
1 . 设置子进程为守护主进程， 主进程推出了，子进程就会销毁， 子进程会依赖主进程
2 . 在主进程推出之前， 让子进程先销毁 
'''