import multiprocessing


# 创建信息展示的任务
def show_info(name, age):
    print(f'你的名字是{name},你的年龄是{age}')

# 创建子进程
# 元组传入参数
# sub_info = multiprocessing.Process(target=show_info, args=('小李',500000000))

# 字典传入参数
# sub_info = multiprocessing.Process(target=show_info, kwargs={'age':20,'name':'王小五'})


# 混合传入参数
sub_info = multiprocessing.Process(target=show_info, args=('小红',), kwargs={'age': 20})

if __name__ == '__main__':
    sub_info.start()
