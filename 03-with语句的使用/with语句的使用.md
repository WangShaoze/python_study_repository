# with语句和上下文管理器的使用
### 1.with语句的使用
**代码块:**
```python
fi = open("yi.txt", "r", encoding="utf-8")
data = fi.read()
print(data)
fi.close()
# 上面的代码要是 yi.txt 文件不存在，就会报错，下面的代码就是改进

# 方法1: 捕获异常

try:
    fo = open("yi.txt", "r", encoding="utf-8")
    fo.write("正好符合四大皆空")
except Exception as e:
    print(e)
finally:
    print("成功关闭文件")
    fi.close()

# 方法2: 使用 with 语句
with open("yi.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
```

### 2.上下文管理器的使用
**代码块:**
```python
# 自定义上下文管理器的实现  __enter__ 和 __exit__  这两个魔法方法
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("over")
        self.file.close()

# with 语句可以配合 上下文管理器 使用
with File("yi.txt", "r") as f:
    # print(f.read())
    f.write("fjdslkaj")
```

### 3.上下文管理器_装饰器的方法事项
**代码块:**
```python
from contextlib import contextmanager


@contextmanager   # 实现上下文管理器的语法糖
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        yield file  # yeild 上面的代码认为是 上文的代码,下面的代码默认是 下文的代码
    except Exception as e:
        print(e)
    finally:
        print("over")
        file.close()

# TypeError: 'generator' object does not support the context manager protocol
# with 语句需要结合上下文管理器,普通的方法不可以
with my_open(file_name="yi.txt", file_mode="r") as f:
    # data = f.read()
    # print(data)
    f.write("hfjakhkdsa")
```

