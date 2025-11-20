# 综合案例2：约瑟夫环问题
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

total_people = 30
need_swimming_people = 15

queue = [0 for _ in range(total_people)]
swimming_people = 0
point = 0
deal_num = 1


def up(point, queue):
    point = (point + 1) % total_people
    if (queue[point] == 1):
       point = up(point, queue)
    return point


while (swimming_people != need_swimming_people):
    print(f"现在是第{point}")
    deal_num += 1
    if (deal_num == 9):
        deal_num = 1
        queue[point] = 1
        swimming_people += 1
        print(f"第{point}死了，一个死了{swimming_people}")
    point = up(point, queue)

print(queue)
