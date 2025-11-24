"""
奥特曼对战小怪兽 - 编程题

题目描述
- 请你实现一个简化版的奥特曼对战小怪兽的游戏。在这个游戏中，奥特曼和小怪兽进行多回合的战斗，直到一方全部死亡。

类设计

- Fighter 类（战斗者基类）
    - 属性：名称(name)、生命值(hp)
    - 方法：
        攻击(attack)：抽象方法，由子类实现
        判断是否存活(alive)：生命值大于0时返回True

- Ultraman 类（奥特曼）
    继承自 Fighter
    新增属性：魔法值(mp)
    方法：
        普通攻击(attack)：对单个敌人造成15-25点伤害
        究极必杀技(huge_attack)：消耗50点魔法值，造成敌人当前生命值3/4或至少50点的伤害
        魔法攻击(magic_attack)：消耗20点魔法值，对所有敌人造成10-15点伤害
        恢复魔法值(resume)：随机恢复1-10点魔法值

- Monster 类（小怪兽）
    继承自 Fighter
    方法：
        攻击(attack)：对单个敌人造成10-20点伤害

任务要求
- 实现上述三个类，确保代码能够正确运行
- 实现游戏主循环，让奥特曼和三个小怪兽进行战斗
- 每个回合，奥特曼随机选择一种攻击方式（普通攻击60%，魔法攻击30%，究极必杀技10%）
- 如果奥特曼的魔法值不足，则使用普通攻击代替
- 每个回合结束后，显示当前战斗状态
- 当一方全部死亡时，游戏结束并宣布胜利者

扩展要求（选做）
- 添加更多类型的奥特曼和小怪兽，具有不同的技能和属性
- 实现玩家可以选择攻击目标或技能的功能
- 添加装备系统，奥特曼和小怪兽可以装备不同的武器和防具
- 实现经验值和升级系统
"""

import random
import time
from enum import Enum, auto
from abc import ABC, abstractmethod
from rich import console

console = console.Console()


class SkillType(Enum):
    ATTACK = auto()
    HUGE_ATTACK = auto()
    MAGIC_ATTACK = auto()
    RESUME = auto()


class Fighter(ABC):
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    @abstractmethod
    def attack(self, targets):
        pass

    def take_damage(self, damage_value):
        self.hp -= damage_value
        if (self.hp < 0):
            self.hp = 0
            console.print(f"[cyan s]{self.name}[/cyan s]")

    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Monster(Fighter):
    def __init__(self, name, hp=100):
        super().__init__(name, hp)

    def attack(self, target: Fighter):
        damage_value = random.randint(10, 20)
        console.print(f"[cyan]{self.name}[/cyan]"
                      f"使用了[bright_red]普通攻击[/bright_red]对[blue]{target.name}[/blue]"
                      f"造成了[bright_red]{damage_value}[/bright_red]点伤害！")
        target.take_damage(damage_value)


class Ultraman(Fighter):
    def __init__(self, name, hp=500, mp=100):
        super().__init__(name, hp)
        self.mp = mp

    def attack(self, targets: list):
        alive_targets = [i for i in targets if i.alive()]
        if (len(alive_targets) == 0):
            return

        target = random.choice(alive_targets)

        skill_weight_list = [0.50, 0.30, 0.10, 0.10]
        skill_type = random.choices(
            list(SkillType), weights=skill_weight_list, k=1)[0]
        match skill_type:
            case SkillType.ATTACK:
                self.use_default_attack(target)
            case SkillType.HUGE_ATTACK:
                self.use_huge_attack(target)
            case SkillType.MAGIC_ATTACK:
                self.use_magic_attack(alive_targets)
            case SkillType.RESUME:
                self.use_resume()

    def use_default_attack(self, target):
        damage_value = random.randint(10, 20)
        console.print(f"[blue]{self.name}[/blue]"
                      f"使用了[bright_red]普通攻击[/bright_red]对[cyan]{target.name}[/cyan]"
                      f"造成了[bright_red]{damage_value}[/bright_red]点伤害！")
        target.take_damage(damage_value)

    def use_huge_attack(self, target):
        if (self.mp >= 50):
            self.mp -= 50
            damage_value = target.hp * 3 / 4
            damage_value = 50 if damage_value < 50 else damage_value
            console.print(f"[blue]{self.name}[/blue]"
                          f"使用了[yellow]究极必杀技[/yellow]对[cyan]{target.name}[/cyan]"
                          f"造成了[yellow]{damage_value:.0f}[/yellow] 点伤害！")
            target.take_damage(damage_value)
        else:
            self.use_default_attack(target)

    def use_magic_attack(self, targets):
        if (self.mp >= 20):
            self.mp -= 20
            damage_value = random.randint(10, 15)
            console.print(f"[blue]{self.name}[/blue]"
                f"使用了[purple]魔法攻击[/purple]对[cyan]所有的怪兽[/cyan]"
                f"造成了[purple]{damage_value}[/purple]点伤害！")
            for target in targets:
                target.take_damage(damage_value)


    def use_resume(self):
        resume_value = random.randint(30, 50)
        self.mp += resume_value
        console.print(f"[blue]{self.name}[/blue]"
                      f"使用了[purple]魔法回复[/purple]恢复了[purple]{resume_value}[/purple]点魔法值！")

    def take_damage(self, damage_value):
        self.hp -= damage_value
        if (self.hp <= 0):
            self.hp = 0
            console.print()
            console.print(f"[b][#FF0909]战斗失败！[/#FF0909] [#782828]{self.name} 已经牺牲！[/#782828] 我们要等待下一次[#FFB109]光[/#FFB109]的降临！[/b]")


def main():
    ultraman = Ultraman("迪迦奥特曼")
    masters = [Monster("哥尔赞"), Monster("美尔巴"), Monster("巴克贡")]
    console.print(f"[blue]{ultraman.name}[/blue]正在和[cyan]{masters[0].name}、{masters[1].name}以及{masters[2].name}[/cyan]战斗！")
    console.print("下面请看现场直播！")
    console.print()
    time.sleep(1)

    i = 0
    while True:
        i += 1
        time.sleep(0.5)
        console.print(f" ----------")
        console.print(f"¦ [b]第[green]{i}[/green]回合[/b] ¦")
        console.print(f" ----------")
        ultraman.attack(masters)
        masters = [i for i in masters if i.alive()]
        if (len(masters) == 0):
            console.print()
            console.print(f"[b] 没有怪兽了, [blue]{ultraman.name}[/blue]赢了[#FFB109]胜利！[/#FFB109][/b]还剩余 [#FF59DB]{ultraman.hp}[/#FF59DB] 点生命值")
            break
        time.sleep(0.5)
        for master in masters:
            time.sleep(0.1)
            master.attack(ultraman)
            if not (ultraman.alive()):
                return

        print()

    time.sleep(15)

if __name__ == "__main__":
    main()
