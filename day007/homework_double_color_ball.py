# 双色球选号器
import random
from rich.console import Console


console = Console()


def get_one():
    red_ball = range(1, 34)
    blue_ball = range(1, 17)

    red = random.sample(red_ball, 6)
    blue = random.sample(blue_ball, 1)

    return {
        "red": sorted(red),
        "blue": blue
    }


def code_rich_str(code):
    return f'[red]{'\t'.join(str(num) for num in code["red"])}[/red]\t[blue]{code["blue"][0]}[/blue]'


success_code = get_one()


console.print(f"中奖号码:{code_rich_str(success_code)}")

count = 0


def code_equals(a, b):
    for i in range(6):
        if (a['red'][i] != b['red'][i]):
            return False
    if (a['blue'][0] != b['blue'][0]):
        return False
    return True


while True:
    count += 1
    luck_code = get_one()
    if code_equals(luck_code, success_code):
        console.clear()
        console.print(
            f"🎉在第[yellow]{count}[/yellow]次买双色球中了一等奖，中奖号码是{code_rich_str(success_code)}, 从此家族兴旺，名震天南数百年！")
        break

    if (count < 10000):
        console.print(
            f"你已经买了[yellow]{count}[/yellow] 次彩票, 号码是:{code_rich_str(luck_code)}", end='\r')
    elif (count % 10000 == 0):
        console.print(
            f"你已经买了[red]{count / 10000:.0f}[/red] 万次彩票, 最新号码是:{code_rich_str(luck_code)}", end='\r')
