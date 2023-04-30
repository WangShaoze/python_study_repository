
fi = open("yi.txt", "r", encoding="utf-8")
data = fi.read()
print(data)
fi.close()


try:
    fo = open("yi.txt", "r", encoding="utf-8")
    fo.write("正好符合四大皆空")
except Exception as e:
    print(e)
finally:
    print("成功关闭文件")
    fi.close()


with open("yi.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
