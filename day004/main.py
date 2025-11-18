# for 循环实习那1~100求和
from random import randint
sum = 0
for i in range(101):
    sum = sum + i
print("∑1~100=", sum)

# for循环实现1~100的偶数求和
sum = 0
for i in range(1, 101, 2):
    sum = sum + i
print("1~100的偶数之和", sum)

# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

ans = randint(1, 100)
user_ans = -1
# while(ans != user_ans):
#     user_ans = int(input("请输入一个数字"))
#     if(ans < user_ans):
#         print("你猜大了")
#     elif(ans > user_ans):
#         print("你猜小了")

print("你猜对了")

# 打印99乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i}x{j}={i*j}")

# 打印99乘法表2
for i in range(1, 10):
    for j in range(1, 10):
        if (j <= i):
            print(f"{j}x{i}={j*i}", end=" ")
    print()

# 判断一个数是不是素数
a = int(input("请输入一个数字, 判断是不是素数"))
b = True
if a <= 2:
    b = False
for i in range(2, a):
    if (a % i == 0):
        b = False
        break
if b:
    print("是")
else:
    print("否")

# 输入两个正数，计算最大公约数和最小公倍数
a = int(input("请输入两个数计算最大公约数和最小公倍数1:"))
b = int(input("请输入两个数计算最大公约数和最小公倍数2:"))

# 辗转相除法计算最大公约数
big = a
small = b
if (b > a):
    big = b
    small = a

c = big % small
while (c != 0):
    big = small
    small = c
    c = big % small
print("最大公约数是", small)

# 最小公倍数 * 最大公约数 = a * b
print("最小公倍数是", a * b / small)


# 打印三角形，入参高度，left | right | big
high = int(input("请输入三角的高度"))
t = input("请输入三角的类型")

if (t == "left"):
    for i in range(high):
        for j in range(high):
            if (j <= i):
                print("*", end="")
        print()
elif (t == "right"):
    for i in range(high):
        for j in range(high):
            if (j <= i):
                print("*", end="")
        print()
elif (t == "big"):
    for i in range(high):
        for j in range(2*high-1):
            if abs(j - (high-1)) <= i:
                print("*", end="")
            elif j<high:
                print(end=" ")
        print()
else:
    print("参数不正确")