import re


# 第一个参数---正则表达式
# 第二个参数---匹配的文本
match_obj = re.match("hel", "hello gehel")
info = match_obj.group()
print(info)

