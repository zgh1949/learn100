# 数据类型有哪些
## 数值
a = 1
b = 1.2
## 字符串
c = 'abc'
## boolean
d = True
e = False


# 运算符
## and or not is
flag1 = 1 > 0
flag2 = 1 < 0

flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1

flag6 = flag1 is True
flag7 = flag1 is not False


# 华氏度转摄氏度  F = 1.8C + 32
f = float(input('请输入华氏度：'))
c = (f - 32) / 1.8
print("%.1f℉ = %.1f℃" % (f, c))

# 计算半径和面积
import math
r = float(input("请输入半径"))
l = 2 * math.pi * r
s = math.pi * r * r
print("r=%.1f, l=%.1f, s=%.1f" % (r, l ,s))

# 输入的年份是不是闰年
year = int(input("请输入年份"))
is_run = (year % 4) == 0 and \
    (year % 100) != 0 or (year % 400) == 0
if(is_run):
    print("%d 是闰年" % (year))
else:
    print(f"{year} 不是闰年")