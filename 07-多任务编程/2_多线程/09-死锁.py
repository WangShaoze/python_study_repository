# 死锁： 一个程序上锁后，因为程序有正常结束没有释放锁

import threading

# 创建锁
Lock = threading.Lock()


# 需求：多个线程根据小标去同一个列表取值，要保证同一时刻只有一个线程去取值
def get_value(index):
    # 上锁
    Lock.acquire()
    my_list = [4, 5, 3]
    # 判断下标是否越界
    if index >= len(my_list):
        print('下标已经越界了。', index)
        # 代码虽然不能正常执行，但是依然要释放锁，不然会影响后面的线程执行
        Lock.release()
        return
    # 根据下表去取值
    value = my_list[index]
    print(value)
    # 释放锁
    Lock.release()


if __name__ == '__main__':
    # 循环创建多个线程
    for i in range(10):
        sub_value = threading.Thread(target=get_value, args=(i,))
        sub_value.start()

'''结论：锁要在合适的地方释放，否则易造成死锁'''
