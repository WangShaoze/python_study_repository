import copy

"""
浅拷贝: 只对可变类型的第一层对象进行拷贝，不对对象进行拷贝，拷贝成功后会开辟新的内存空间存储这个拷贝对象
"""

# 不可变类型  数字，字符串，元组
num1 = 9
num2 = copy.copy(num1)

# 内存地址没有发生变化，说明浅拷贝对不可变类型，只是拷贝了内存地址(引用)，就是实现了赋值的功能
print("num1:", id(num1))
print("num2:", id(num2))

my_tuple = (23, 67)
my_tuple1 = copy.copy(my_tuple)
print("my_tuple:", id(my_tuple))
print("my_tuple1:", id(my_tuple1))

my_str = "你好， 四hi"
my_str1 = copy.copy(my_str)
print("my_str:", id(my_str))
print("my_str1:", id(my_str1))

# 可变类型：列表，字典，集合
my_list = [1, 3, 23, 2, [34, 567, 76], [78, 89]]
my_list1 = copy.copy(my_list)
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
