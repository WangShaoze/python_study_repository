import multiprocessing
import time

# 声明全局变量----创建一个添加数据的列表
glo_list = list()


# 添加数据的函数
def add_data():
    for i in range(6):
        glo_list.append(i)
        print('add:', i)
        time.sleep(0.9)
    print('数据添加完成。', glo_list)


# 添加数据的函数
def read_data():
    print('读取到的数据为：', glo_list)


# 添加数据的子进程
add_process = multiprocessing.Process(target=add_data)

# 读取数据的子进程
read_process = multiprocessing.Process(target=read_data)


if __name__ == '__main__':
    # 启动子进程
    add_process.start()
    add_process.join()
    time.sleep(3)
    print('main Processing', glo_list)
    read_process.start()
