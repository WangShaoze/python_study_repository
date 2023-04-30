import copy
"""
深拷贝: 拷贝可变类型数据所有层的数据，并生成相应的空间
"""

# 不可变类型  数字，字符串，元组
num1 = 9
num2 = copy.deepcopy(num1)

# 内存地址没有发生变化，说明浅拷贝对不可变类型，只是拷贝了内存地址(引用)，就是实现了赋值的功能
print("num1:", id(num1))
print("num2:", id(num2))

my_tuple = (23, 67)
my_tuple1 = copy.deepcopy(my_tuple)
print("my_tuple:", id(my_tuple))
print("my_tuple1:", id(my_tuple1))

print("--------------------------")
my_tuple = (23, 67, [34, 54, 65, [47, 78]])  # 内部含有可变类型，就会对对象和所有子元素进行拷贝
my_tuple1 = copy.deepcopy(my_tuple)
print("my_tuple:", id(my_tuple))
print("my_tuple1:", id(my_tuple1))
print("my_tuple[0]:", id(my_tuple[0]))
print("my_tuple1[0]:", id(my_tuple1[0]))
print("my_tuple[2]:", id(my_tuple[2]))
print("my_tuple1[2]:", id(my_tuple1[2]))


# 可变类型：列表，字典，集合
my_list = [1, 3, 23, 2, [34, 567, 76], [78, 89]]
my_list1 = copy.deepcopy(my_list)
print("my_list:", my_list)
print("my_list1:", my_list1)
print("my_list_id:", id(my_list))
print("my_list1_id:", id(my_list1))

print("-----------------------")
my_list.append(111)
print("my_list:", my_list)
print("my_list1:", my_list1)
print("my_list_id:", id(my_list))
print("my_list1_id:", id(my_list1))

print("-----------------------")
my_list[4].append(111)
print("my_list:", my_list)
print("my_list1:", my_list1)
print("my_list:", my_list[4])
print("my_list1:", my_list1[4])
print("my_list[4]_id:", id(my_list[4]))
print("my_list1[4]_id:", id(my_list1[4]))