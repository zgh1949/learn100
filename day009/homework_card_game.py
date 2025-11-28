"""
扑克牌游戏 - 编程题

题目描述
- 请你实现一个简单的扑克牌游戏程序，模拟一副扑克牌的洗牌、发牌和玩家整理手牌的过程。

类设计
- Card 类（单张扑克牌）
    属性：花色(suite)、点数(face)
    方法：
        字符串表示方法(__str__和__repr__)：将扑克牌转换为可读的字符串格式
- Poker 类（一副扑克牌）
    属性：牌组(cards)、当前发牌位置(current)
    方法：
        洗牌(shuffle)：将牌随机打乱顺序
        发牌(next)：按顺序发下一张牌
        判断是否还有牌(has_next)：检查是否还有牌可发
- Player 类（玩家）
    属性：姓名(name)、手牌(cards_on_hand)
    方法：
        摸牌(get)：从牌堆获取一张牌
        整理手牌(arrange)：按照指定规则对手牌进行排序

任务要求
- 实现上述三个类，确保代码能够正确运行
- 实现扑克牌的初始化，包含52张牌（4种花色，每种花色13张牌）
- 实现洗牌功能，将牌随机打乱
- 实现发牌功能，将牌平均发给4个玩家（每人13张）
- 实现手牌排序功能，按照花色和点数排序
- 显示每个玩家的手牌

扩展要求（选做）
- 添加扑克牌游戏规则，如比较牌面大小、判断牌型等
- 实现多种排序规则（如按点数优先、按花色优先等）
- 添加更多玩家，并实现不同的发牌方式
- 实现扑克牌游戏的图形界面
"""
from enum import Enum
import random
import rich
from rich.console import Console

console = Console(highlight=False)


class Suite(Enum):
    hearts = (0, "♥", "[red]♥[/red]",)
    spades = (1, "♠", "[blue]♠[/blue]")
    diamonds = (2, "♦", "[red]♦[/red]")
    clubs = (3, "♣", "[blue]♣[/blue]")

    def __init__(self, code, sign, rich_text):
        self.code = code
        self.sign = sign
        self.rich_text = rich_text


face_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, face, suite: Suite):
        self.face = face
        self.suite = suite

    def __str__(self):
        if self.suite and hasattr(self.suite, 'sign'):
            return self.suite.rich_text + str(self.face)
        else:
            return str(self.face)

    def __repr__(self):
        return self.__str__()


class Poker:
    def __init__(self, cards=None, current=0):
        if cards is None or len(cards) == 0:
            cards = []
            for i in face_list:
                for j in Suite:
                    cards.append(Card(i, j))

        self._cards = cards
        self._current = current

    def size(self):
        return len(self._cards)

    def shuffle(self):
        """洗牌"""
        current = 0

        for i in range(len(self._cards)-1, 0-1, -1):
            j = random.randint(0, i)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]

    def next(self):
        """发牌"""
        if (self.has_next()):
            self._current += 1
            return self._cards[self._current - 1]
        return None

    def has_next(self):
        """判断是否还有牌"""
        return self._current < len(self._cards)

    def print(self, message):
        console.print(message)
        for i in self._cards:
            console.print(f"{i}", end=" ")
        console.print()


class Player:
    def __init__(self, name):
        self._name = name
        self._cards = []

    def get(self, poker: Poker):
        """摸牌"""
        if (poker.has_next()):
            self._cards.append(poker.next())

    def arrange(self):
        self._cards = sorted(self._cards, key=lambda x: (face_list.index(x.face), x.suite.code))

    def __str__(self):
        return f"{self._name}:{" ".join([str(x) for x in self._cards])}"


if __name__ == "__main__":
    poker = Poker()
    poker.print("这是一副新牌")

    poker.shuffle()
    poker.print("洗牌")

    player1 = Player("玩家1")
    player2 = Player("玩家2")
    player3 = Player("玩家3")
    player4 = Player("玩家4")

    players = [player1, player2, player3, player4]
    index = 0

    while (poker.has_next()):
        index = (index+1) % 4
        players[index].get(poker)

    for player in players:
        player.arrange()
        console.print(f"{player}" )

    while True:
        pass