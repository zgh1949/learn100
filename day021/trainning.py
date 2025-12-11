# 读取文件
try:
    file1 = open("day011/abc.txt", "r", encoding="utf-8")
    print(file1.read())
    file1.close()
    print()
except FileNotFoundError:
    print("文件未找到")
except LookupError:
    print("指定的文件编码出错")
except UnicodeDecodeError:
    print("读取文件时解码出错")


try:
    file2 = open("day011/abc.txt", "r", encoding="utf-8")
    for line in file2.readlines():
        print(line, end="")
    file2.close()
except FileNotFoundError:
    print("文件未找到")
except LookupError:
    print("指定的文件编码出错")
except UnicodeDecodeError:
    print("读取文件时解码出错")

# 写入文件
try:
    file3 = open("day011/abc.txt", "a", encoding="utf-8")
    file3.write("【添加字段】")
    file3.close()
except FileNotFoundError:
    print("文件未找到")
except LookupError:
    print("指定的文件编码出错")
except UnicodeDecodeError:
    print("读取文件时解码出错")

# 复制二进制文件
try:
    with open("day011/python-logo.png", "rb") as source, open("day011/python-logo2.png", "ab") as target:
        size = 1024 * 10
        data = source.read(size)
        while data:
            target.write(data)
            data = source.read(size)
except FileNotFoundError:
    print("文件未找到")
except IOError as e:
    print("IO出错", e)


# 给上面都加上异常处理
