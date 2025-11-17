# 厘米和英寸的转换  1in = 2.54cm
import math
from random import randint
val = float(input("请输入要转换的值"))
unit = input("请输入单位")
if (unit == 'in' or unit == '英寸'):
    print(f"{val}{unit} = %f%s" % (val * 2.54, "cm"))
elif (unit == 'cm' or unit == "厘米"):
    print(f"{val}{unit} = %f%s" % (val / 2.54, "in"))
else:
    print("不支持的单位")


# 掷筛子决定做什么
val = randint(1, 6)
if (1 == val):
    print("吃饭")
elif (2 == val):
    print("睡觉")
elif (3 == val):
    print("打豆豆")
elif (4 == val):
    print("再次打豆豆")
elif (5 == val):
    print("再再打一遍")
elif (6 == val):
    print("再再再打一次")
else:
    print("错误事件")

# 成绩等级
score = float(input("请输入成绩"))
if (score < 60):
    print("不及格")
elif (score < 70):
    print("NPC")
elif (score < 80):
    print("普通人")
elif (score < 90):
    print("人上人")
else:
    print("夯")

# 三条边能否构成三角形，如果能够成就计算其面积
a = float(input("请输入边1长度："))
b = float(input("请输入边2长度："))
c = float(input("请输入边3长度："))

if (a <= 0 or b <= 0 or c <= 0):
    print("不能构成三角形")
elif (a >= b + c or b >= a + c or c >= a + b):
    print("不能构成三角形")
else:
    s = (a + b + c) / 2
    A = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print("边长 %f,%f,%f 可以构成三角形，面积是%f" % (a, b, c, A))

# 个人所得税计算器 
money = float(input("请输入你的工资"))
money_need_tax = money - 60000
print("您要交税的额度是：")
if(money_need_tax < 36000):
    print(money_need_tax * 0.03 -0)
elif(money_need_tax < 144000):
    print(money_need_tax * 0.1 - 2520)
elif(money_need_tax < 300000):
    print(money_need_tax * 0.2 - 16920)
else:
    ans = input('你有那么高的工资吗？y/n')
    if('y' == ans):
        print("收我做小弟吧")
    else:
        print("滚")



