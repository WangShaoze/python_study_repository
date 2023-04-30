import re

my_fruit = ["苹果", "李子", '梨', '葡萄', '山竹', '香蕉']

# | : 表示左右两个任意一个都可以
for uni in my_fruit:
    match_obj = re.match("葡萄|香蕉", uni)
    if match_obj:
        print("是我想要的:", match_obj.group(), '----------------->')
    else:
        print("不是我想吃的:", uni)

'''
匹配163，126，qq邮箱：
    @ 前面是 数字下划线 大小写英文字母  出现 4 为到 20 位
    @ 后面是 163.com , 126.com , qq.com
'''
# (qq|163|126) 表示一个分组,里面的任意一个表达式出现在相应的位置就可以，这里代表的是第1个分组
# \.  : 表示一个真实的 .
match_obj = re.match('[a-zA-Z0-9_]{4,20}@(qq|163|126)\.com', 'xioHu_89033@163.com')
if match_obj:
    print(match_obj.group())
else:
    print("没有合法邮箱。")

# ([a-zA-Z0-9_]{4,20})  这里代表的是第2个分组
# (qq|163|126) 表示一个分组,里面的任意一个表达式出现在相应的位置就可以，这里代表的是第2个分组
# \.  : 表示一个真实的 .
match_obj = re.match('([a-zA-Z0-9_]{4,20})@(qq|163|126)\.com', 'xioHu_89033@163.com')
if match_obj:
    result = match_obj.group(0)  # 默认就是第0个分组,可以不用写
    email_user = match_obj.group(1)
    email_type = match_obj.group(2)
    print("name:{}, type:{}, email:{}".format(email_user, email_type, result))
else:
    print("没有合法邮箱。")

# qq:343555548
match_obj = re.match('(qq):([1-9]\d{5,9})', 'qq:343555548')
if match_obj:
    email_type = match_obj.group(1)
    email_number = match_obj.group(2)
    print("name:{}, type:{}".format(email_number, email_type))
else:
    print("没有合法邮箱。")

# \num :  \1 代表引用第一个分组的数据,需要注意的是，这里的 \1 是一个整体，其中的的 \ 是一个普通的 \, 需要使用转义字符进行转义
# <html>hh,你好</html>
match_obj = re.match('<([a-zA-Z1-6]+)>.*</\\1>', '<html>hh,你好</html>')
if match_obj:
    print(match_obj.group())
else:
    print("没有合法邮箱。")


# <html><div>hh,你好</div></html>   # 出现多个分组时，需要注意引用分组的顺序问题
match_obj = re.match('<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>', '<html><div>hh,你好</div></html>')
if match_obj:
    print(match_obj.group())
else:
    print("没有合法邮箱。")

####################################
# 给分组取别名 (?P<name>正则表达式)  需要引用分组的时候，可以用 取好的别名
# <html><div>hh,你好</div></html>
match_obj = re.match('<(?P<label_html>[a-zA-Z1-6]+)><(?P<lable_div>[a-zA-Z1-6]+)>(?P<content>.*)</(?P=lable_div)></(?P=label_html)>', '<html><div>hh,你好</div></html>')
if match_obj:
    print(match_obj.group("label_html"))
    print(match_obj.group("lable_div"))
    print(match_obj.group("content"))
else:
    print("没有合法邮箱。")

