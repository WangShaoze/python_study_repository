"""
2中创建方式:
1.将列表推导式中的 中括号 改为 小口号
2. 只要函数中存在 yeild 那么,可以认为这个函数是 生成器
"""

# my_generator = (uni*2 for uni in range(3))
# print(my_generator)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))   # 当生成器没有值的时候,就会抛出 StopIteration 异常,表示生成器生成的数据完毕

# my_generator = (uni*2 for uni in range(3))
# # 使用 while 循环
# while True:
#     try:
#         print(next(my_generator))
#     except Exception as e:
#         print(e)
#         break


my_generator = (uni*2 for uni in range(3))

# for 循环内部会自动调用 next() 函数,获取生成器的值.当生成器数据生成完毕,for 会自动 捕获异常 结束循环
for value in my_generator:
    print(value)
