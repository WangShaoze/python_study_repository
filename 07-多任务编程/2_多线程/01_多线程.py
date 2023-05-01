# 导入线程的包
import threading


def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print(f'当前线程是{current_thread}')
    for i in range(5):
        print('唱歌中...')


def dance():
    # 获取当前线程
    current_thread = threading.current_thread()
    print(f'当前线程是{current_thread}')
    for i in range(5):
        print('跳舞中...')


if __name__ == '__main__':
    # 获取当前线程
    current_thread = threading.current_thread()
    print(f'当前线程(主线程)是{current_thread}')

    # 创建子线程
    sing_thread = threading.Thread(target=sing, name=' sing_thread')
    dance_thread = threading.Thread(target=dance, name='dance_thread')

    # 开始子线程
    sing_thread.start()
    dance_thread.start()

