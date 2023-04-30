import re

# * : 前面一个字符出现0次或者无限次,即 可有可无
match_obj = re.match("t.*o", "tfdsafdsa5o")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')


# + : 前面一个字符出现1次或者无限次,即 被 修饰的字符 至少有一个
# match_obj = re.match("t.+o", "to")   # None
match_obj = re.match("t.+o", "t范德萨范德萨rro")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')

# ? : 前面一个字符出现0次或者1次,即 被 修饰的字符 要么 没有，有也只能有一个
match_obj = re.match("https?", "http")
# match_obj = re.match("https?", "https")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')


# {m} : 前面一个字符必循出现m次
match_obj = re.match("ht{2}}ps?", "http")
# match_obj = re.match("ht{2}}ps?", "htttp")   # 没有匹配的字符。
# match_obj = re.match("ht{2}ps?", "https")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')

print("-------------------------------------------")
# {m,n} : 前面一个字符必循出现m次到n次
# match_obj = re.match("ht{1,5}ps?", "http")
# match_obj = re.match("ht{1,5}ps?", "htp")
match_obj = re.match("ht{1,5}ps?", "htttttps")
# match_obj = re.match("ht{1,5}ps?", "httttttttttttttttp")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')

# {3,} : 至少出现 3 次
# match_obj = re.match("ht{3,}ps?", "https")  # 没有匹配的字符。
match_obj = re.match("ht{1,5}ps?", "httttttttttttttttp")
if match_obj:
    print(match_obj.group())
else:
    print('没有匹配的字符。')
