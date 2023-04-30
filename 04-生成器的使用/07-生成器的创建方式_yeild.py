def my_generator():
    for i in range(4):
        print("开始生成数据了...")
        yield i   # 每一次输出的时候,程序会暂停
        print("上一次数据生成完毕.")


result = my_generator()
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)

# value = next(result)   # 所有数据生成完毕 后 如果在调 就 StopIteration
# print(value)


for i in result:
    print(i)

