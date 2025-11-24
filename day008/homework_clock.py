# 练习1：定义一个类描述数字时钟
import time
from rich.console import Console

console = Console()


class Clock:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def addHour(self, n=0):
        self.h = (self.h+n) % 24

    def addMinute(self, n=0):
        sum_minute = self.m + n
        while (sum_minute >= 60):
            self.addHour(1)
            sum_minute -= 60
        self.m = sum_minute

    def addSecond(self, n=0):
        sum_second = self.s + n
        while (sum_second >= 60):
            self.addMinute(1)
            sum_second -= 60
        self.s = sum_second

    def to_str(self, num):
        if (num < 10):
            return "0"+str(num)
        else:
            return str(num)

    def printTime(self):
        console.print(f"[red]{self.to_str(self.h)}[/red][white]:[/white]" +
                      f"[blue]{self.to_str(self.m)}[/blue][white]:[/white]" +
                      f"[yellow]{self.to_str(self.s)}[/yellow]")


if __name__ == "__main__":
    c = Clock(10, 30, 0)
    c.printTime()
    c.addSecond(100)
    c.printTime()
    c.addSecond(80)
    c.printTime()
    c.addMinute(24*60)
    c.printTime()
