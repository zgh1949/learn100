# 计算两枚骰子投出的结果与概率
from random import randint
table = {}
for i in range(1, 7):
    for j in range(1, 7):
        sum_two = i + j
        if sum_two in table:
            table[sum_two] += 1
        else:
            table[sum_two] = 1

for k, v in table.items():
    print(f"k={k},v={v},p={v/36 * 100:.2f}%")

# craps 游戏
# 规则，掷两枚骰子，按照点数判断输赢
# 1.出场：（第一次投掷）
# 7/11 立即赢
# 2/3/12 立即输
# 4/5/6/8/9/10 进入点数游戏
# 2.点数阶段（第二次投掷）
# 再次投出相同点数的数 赢
# 投出7 输
# 其他数 重复第二轮
def roll():
    a = randint(1, 6)
    b = randint(1, 6)
    # print("掷出了",a+b)
    return a + b


def play():
    point = roll()
    if (point == 7 or point == 11):
        print("Win!")
        return True
    elif (point == 2 or point == 3 or point == 12):
        print("Craps!")
        return False
    else:
        while True:
            point2 = roll()
            if point2 == point:
                print("Win!")
                return True
            elif point2 == 7:
                print("Craps")
                return False

play()
n = 1000000;
win = 0
for i in range(n):
    if(play()):
        win += 1
    
win_rate = win/n

print(f"{n}次总结出的胜率{win_rate*100:.2f}%")
print(f"庄家优势为{(0.5-win_rate)*2*100:.2f}%")