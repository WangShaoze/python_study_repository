# 1.导入进程包
import multiprocessing
import time


# 定义跳舞这个任务
def dance():
    for i in range(10):
        print('跳舞中...')
        time.sleep(0.4)
    print('完成跳舞任务。')


# 定义唱歌这个任务
def sing():
    for i in range(10):
        print('唱歌中...')
        time.sleep(0.4)
    print('完成唱歌任务。')


# 2.创建子进程(自己手动创建的进程是子进程，默认创建的那个进程是主进程, __init__.py中已经将Process类导入)
'''
参数：
1.group 进程组----一般不设置---默认为None
2.target 执行的任务的函数或方法(目标任务) ------ target=dance 这里任务是对函数的引用，不是调用
3.name 进程名----一般不设置----默认为process-1，process-2.....
'''
dace_processing = multiprocessing.Process(group=None, target=dance)
sing_processing = multiprocessing.Process(group=None, target=sing)


if __name__ == '__main__':
    # 3.启动进程执行任务
    sing_processing.start()
    dace_processing.start()
    """
    多进程的调度是无序的，具体先调用谁，有操作系统决定
    """
    # # 创建主进程
    # sing()

'''
先创建了一个主进程-----在主进程中、
又创建了----两个子进程
'''
