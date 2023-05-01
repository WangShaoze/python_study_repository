import multiprocessing
import time

# 声明全局变量 -- 列表
glo_list = list()


# 添加数据的任务
def add_data():
    for i in range(3):
        glo_list.append(i)
        print('add:', i)
        time.sleep(0.8)
    print('数据添加完成。', glo_list)


# 读取数据的任务
def read_data():
    print('读取的数据为：', glo_list)


# 添加数据的子进程
add_process = multiprocessing.Process(target=add_data)
# 读取数据的子进程
read_process = multiprocessing.Process(target=read_data)


if __name__ == "__main__":
    # 启动进程执行相应的任务
    add_process.start()
    add_process.join()  # 设置进程等待，主进程等待， 数据添加的进程完成之后，在继续往下执行代码
    print('main processing :', glo_list)  # 读取全局变量中的 数据
    read_process.start()


# 结论：进程之间不共享全局变量
# 子进程之间与子进程和主进程是不会 共享全局变量的
# 子进程 建立 分配的是主进程的 内存
# 子进程 对主 进程的数据 进行 拷贝----拷贝的是所有的函数和方法
