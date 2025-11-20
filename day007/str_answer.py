s = "hello world!"

# 计算字符串的长度
print(len(s))

# 获得字符串首字母大写的拷贝
print(s.capitalize())

# 获得字符串变大写后的拷贝
print(s.upper())

# 从字符串中查找子串所在位置
print(s.find("world"))

# 与find类似但找不到子串时会引发异常
print(s.index("world"))

# 检查字符串是否以指定的字符串开头
print(s.startswith("hello"))

# 检查字符串是否以指定的字符串结尾
print(s.endswith("!"))

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(s.center(50, '*'))

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(s.rjust(50, " "))
print(s.ljust(50, "_"))

# 从字符串中取出指定位置的字符(下标运算)
print(s[4])

# 字符串切片(从指定的开始索引到指定的结束索引)
print(s[:])
print(s[1:])
print(s[:-1])
print(s[::1])
print(s[::2])
print(s[1:-1:2])

# 检查字符串是否由数字构成
print(s.isdigit())

# 检查字符串是否以字母构成
print(s.isalpha())

# 检查字符串是否以数字和字母构成
print(s.isalnum())

# 获得字符串修剪左右两侧空格的拷贝
print(s.strip())
