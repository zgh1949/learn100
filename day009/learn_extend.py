# 继承与抽象类

# python的抽象类要从abc（Abstract Base Classes）中导入
from abc import ABC, abstractmethod


class Person(ABC): # 抽象类要继承
    """人，集成object"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def play(self):
        print(f"{self._name} 正在玩游戏")

    @abstractmethod
    def drive(self):
        pass


class Student(Person):
    def play(self):
        print(f"{self._name} 正在玩沙包")

    def drive(self):
        print(f"{self._name} 正在开玩具车")


class Boss(Person):
    def play(self):
        print(f"{self._name} 正在玩xx")

    def drive(self):
        print(f"{self._name} 正在开奔驰车")


p = Boss("老李", 48)
p.play()

s = Student("小明", 13)
s.play()
