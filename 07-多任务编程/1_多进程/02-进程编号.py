# 1.导入包
import multiprocessing
import time
import os


# 定义跳舞这个任务
def dance():
    # 获取当前（子进程）进程编号
    dance_process_id = os.getpid()
    # 获取当前进程的对象，
    print('dance_process_id:', dance_process_id, multiprocessing.current_process())
    # 获取当前子进程对应父进程的编号
    dance_parent_id = os.getppid()
    print('dance_parent_id父进程编号:', dance_parent_id)
    for i in range(10):
        print('跳舞中...')
        time.sleep(0.4)
    print('完成跳舞任务。')


# 定义主进程的任务
def sing():
    # 获取当前（子进程）进程编号
    sing_process_id = os.getpid()
    # 获取当前进程的对象，
    print('sing_process_id:', sing_process_id, multiprocessing.current_process())
    # 获取当前子进程的父进程编号
    sing_parent_id = os.getppid()
    print('sing_parent_id父进程编号:', sing_parent_id)
    for i in range(10):
        print('唱歌中...')
        time.sleep(0.4)
        # 假设我们只需要让它执行一次，就将它杀死
        os.kill(sing_process_id, 9)
    print('完成唱歌任务。')


if __name__ == '__main__':
    # 获取当前（主进程）进程编号
    main_process_id = os.getpid()
    # 获取当前（主进程）进程的对象
    print('main_process_id:', main_process_id, multiprocessing.current_process())
    # 2.创建子进程
    dance_processing = multiprocessing.Process(group=None, target=dance, name='dance')
    sing_processing = multiprocessing.Process(target=sing, name='sing')
    # 3.开始子进程执行任务
    dance_processing.start()
    sing_processing.start()
