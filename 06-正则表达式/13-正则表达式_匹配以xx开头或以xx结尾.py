import re

# 匹配以数字开头
# match_obj = re.match("^\d.*", "asdfdsafd")  # None
match_obj = re.match("^\d.*", "1232asdfdsafd")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。 match_obj == None')

# 匹配以数字结尾
# match_obj = re.match(".*\d$", "asdfdsafd")  # None
match_obj = re.match(".*\d$", "asdfdsafd43434")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。 match_obj == None')


# 匹配以 _ 开头,匹配以数字结尾
# match_obj = re.match("^_.*\d$", "asdfdsafd43434")  # None
# match_obj = re.match("^_.*\d$", "_asdfdsafd")   # None
match_obj = re.match("^_.*\d$", "_asdfdsafd43434")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。 match_obj == None')


# [^指定字符] : 表示除了指定字符以外的字符都可以
# match_obj = re.match("^[^sd]", "sdddfds")   # None
# match_obj = re.match("^[^4F]", "sdddfds")
match_obj = re.match("^\d.*[^095]$", "0023fsafdsafd8")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。 match_obj == None')