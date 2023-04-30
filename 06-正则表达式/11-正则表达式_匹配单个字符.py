import re

# match_obj = re.match("t.o", "two")
match_obj = re.match("t.o", "t\no")
# match_obj = re.match("t.o", "tko")
if match_obj:
    print(match_obj.group())
else:
    # match_obj ----------> None
    print("没有符合要求的匹配结果。")

# match_obj = re.match("葫芦娃[123456]", "葫芦娃3")
match_obj = re.match("葫芦娃[123456]", "葫芦娃4")
# match_obj = re.match("葫芦娃[123456]", "葫芦娃7")
if match_obj:
    print(match_obj.group())
else:
    # match_obj ----------> None
    print("没有符合要求的匹配结果。")

# 匹配银行卡中的 一位 数
# match_obj = re.match("[023456789]", "6")
match_obj = re.match("[0-9]", "6")
# match_obj = re.match("\d", "6")    # '\d' <==============> '[0123456789]'
# match_obj = re.match("\D", "6")    # '\D' <==============> 非'[0123456789]'
if match_obj:
    print(match_obj.group())
else:
    # match_obj ----------> None
    print("没有符合要求的匹配结果。")

"""
\s: 一个空格，\t \n
\S: 非 \t \n 和空格
"""
# match_obj = re.match("葫芦娃 \d", "葫芦娃 7")
# match_obj = re.match("葫芦娃\t\d", "葫芦娃\t7")
# match_obj = re.match("葫芦娃\n\d", "葫芦娃\n7")
match_obj = re.match("葫芦娃\s\d", "葫芦娃 7")
# match_obj = re.match("葫芦娃\s\d", "葫芦娃\n7")
# match_obj = re.match("葫芦娃\s\d", "葫芦娃\t7")
if match_obj:
    print(match_obj.group())
else:
    # match_obj ----------> None
    print("没有符合要求的匹配结果。")

# 匹配某网站的密码中的其中一位，密码组成:大写字母小写字母数字下划线
# match_obj = re.match("[a-zA-Z0-9_]", "5")
# match_obj = re.match("[a-zA-Z0-9_]", "a")
# match_obj = re.match("[a-zA-Z0-9_]", "F")
match_obj = re.match("[a-zA-Z0-9_]", "_")  # [a-zA-Z0-9_]  <=============> \w - 汉字
# match_obj = re.match("\w", "_")  #  \w:  [a-zA-Z0-9_] 和 汉字
# match_obj = re.match("\W", "（")  # \W:  非‘[a-zA-Z0-9_] 和 汉字’
if match_obj:
    print(match_obj.group())
else:
    # match_obj ----------> None
    print("没有符合要求的匹配结果。")
