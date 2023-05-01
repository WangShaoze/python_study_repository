# 1.导入进程包
import multiprocessing
import os
import time


# 定义跳舞这个任务
def dance():
    # 获取当前进程(子进程)的编号
    dance_process_id = os.getpid()
    process_name = multiprocessing.current_process()
    print('dance进程编号为：', dance_process_id, process_name)
    # 获取父进程编号
    parent_id = os.getppid()
    print('dance父进程编号为', parent_id)
    for i in range(10):
        print('跳舞中...')
        time.sleep(0.4)
    print('完成跳舞任务。')


# 定义唱歌这个任务
def sing():
    # 获取当前进程(子进程)的编号
    sing_process_id = os.getpid()
    process_name = multiprocessing.current_process()
    print('sing进程编号为：', sing_process_id, process_name)
    # 获取父进程编号
    parent_id = os.getppid()
    print('sing父进程编号为', parent_id)
    for i in range(10):
        print('唱歌中...')
        # 杀死一个进程--根据进程编号-杀死进程
        os.kill(sing_process_id, 9)
        time.sleep(0.4)
    print('完成唱歌任务。')


# 2.创建子进程(自己手动创建的进程是子进程，默认创建的那个进程是主进程, __init__.py中已经将Process类导入)
dace_processing = multiprocessing.Process(group=None, target=dance)
sing_processing = multiprocessing.Process(group=None, target=sing)


if __name__ == '__main__':
    # 获取当前进程(主进程)的编号
    main_process_id = os.getpid()
    name_process = multiprocessing.current_process()
    print('主进程编号为：', main_process_id, name_process)
    # 3.启动进程执行任务
    sing_processing.start()
    dace_processing.start()
