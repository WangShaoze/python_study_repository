import multiprocessing


def show_info(name, age):
    print(f'姓名是：{name}, 年龄是：{age}')

# 以元组的方式传参
# sub_process = multiprocessing.Process(target=show_info, args=('小王', 22))


# 以字典的方式传参
# sub_process = multiprocessing.Process(target=show_info, kwargs={'name': '小王', 'age': 22})


# 混合传参
sub_process = multiprocessing.Process(target=show_info, args=('小王',), kwargs={'age': 22})

if __name__ == '__main__':
    sub_process.start()
