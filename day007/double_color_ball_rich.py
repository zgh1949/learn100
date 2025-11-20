# 双色球选号器
import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

# 创建控制台对象
console = Console()

def get_one():
    """生成单注双色球号码"""
    # 红球范围1-33，蓝球范围1-16
    red_ball = range(1, 34)
    blue_ball = range(1, 17)
    
    # 随机选择6个不重复的红球和1个蓝球
    red = random.sample(red_ball, 6)
    blue = random.sample(blue_ball, 1)
    
    return {
        "red": sorted(red),  # 红球排序
        "blue": blue
    }

def get_nums(n):
    """生成n注双色球号码"""
    return [get_one() for _ in range(n)]

def code_equals(a, b):
    """比较两注号码是否相同"""
    # 比较红球
    for i in range(6):
        if a['red'][i] != b['red'][i]:
            return False
    # 比较蓝球
    if a['blue'][0] != b['blue'][0]:
        return False
    return True

def celebrate_win(console, count, success_code):
    """创建中奖庆祝效果"""
    # 清屏
    console.clear()
    
    # 创建庆祝文本（移除emoji）
    title = Text("=== 恭喜中奖！ ===", style="bold red")
    
    # 中奖信息
    win_info = Text(f"你在第 {count} 次购买双色球中了1等奖！", style="bold green")
    
    # 号码信息（确保数字格式化为两位显示）
    red_balls = " ".join([f"{ball:02d}" for ball in success_code['red']])
    blue_ball = f"{success_code['blue'][0]:02d}"
    numbers = Text(f"中奖号码: 红球 [red]{red_balls}[/red] 蓝球 [blue]{blue_ball}[/blue]", style="bold")
    
    # 创建面板（使用纯文本装饰）
    panel = Panel(
        Align.center(
            Text.from_markup(
                "\n".join([
                    "",
                    str(title),
                    "",
                    str(win_info),
                    "",
                    str(numbers),
                    "",
                    "**********************************",
                    "*             恭喜发财           *",
                    "**********************************",
                    "本次中奖预计在" + str(int(count / 52 / 3)) + "年后",
                    "恭喜你获得了大量修仙资源，为成为金丹修士创造了良好的基础，道阻且长，道友加油",
                    ""
                ])
            )
        ),
        title="双色球一等奖",
        border_style="bright_yellow",
        padding=(1, 2)
    )
    
    # 显示面板
    console.print(panel)
    

# 生成中奖号码
success_code = get_one()

# 格式化显示中奖号码
formatted_red = " ".join([f"{ball:02d}" for ball in success_code['red']])
formatted_blue = f"{success_code['blue'][0]:02d}"
console.print(f"[bold green]目标号码:[/bold green] 红球 [red]{formatted_red}[/red] 蓝球 [blue]{formatted_blue}[/blue]")

count = 0

# 模拟购买彩票的主循环
console.print("开始模拟购买彩票...\n")
while True:
    count += 1
    # 生成随机号码
    luck_code = get_one()
    
    # 检查是否中奖
    if code_equals(luck_code, success_code):
        celebrate_win(console, count, success_code)
        break  # 中奖后退出循环
    
    # 每10000次显示一次购买次数
    if count % 10000 == 0:
        console.print(f"你已经买了 [bold red]{count/10000:.0f}[/bold red] 万次彩票了", end="\r")

# 程序结束提示
input("按回车键退出...")