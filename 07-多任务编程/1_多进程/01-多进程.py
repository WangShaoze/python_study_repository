#1.导入包
import multiprocessing
import time

#定义跳舞这个任务
def dance():
    for i in range(10):
        print('跳舞中...')
        time.sleep(0.4)
    print('完成跳舞任务。')
#定义主进程的任务
def sing():
    for i in range(10):
        print('唱歌中...')
        time.sleep(0.4)
    print('完成唱歌任务。')
#2.创建子进程#
'''
参数：
1.group 进程组----一般不设置---默认为None
2.target 执行的任务的函数或方法(目标任务)
3.name 进程名----一般不设置----默认为process-1，process-2.....
'''
dance_processing = multiprocessing.Process(group=None,target=dance)


if __name__ == '__main__':
    # 3.开始子进程执行任务
    dance_processing.start()
    # 创建主进程
    sing()

'''
结论：先执行主进程，后执行子进程
'''