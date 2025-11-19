# 水仙数
# 指每个数位上的数字的3次幂之和等于其本身的三位数，如153=1³+5³+3³

# 拆分数字
def splitNum(num):
    array = []
    while (num > 0):
        p = num % 10
        num = int(num / 10)
        array.append(p)
    return array

# 检查是否满足
def check(num, array):
    sum = 0
    for i in array:
        sum += i**3
    return sum == num


n = int(input("请输入n"))

for i in range(1, n+1):
    array = splitNum(i)
    if (check(i, array)):
        print(">", i)
