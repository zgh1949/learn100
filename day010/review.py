# 🟡Day001

# 学习了trutle 海龟图形编辑器
from abc import ABC, abstractmethod
from enum import Enum, auto
import time
from rich.console import Console
from captcha.image import ImageCaptcha
import math as ms
import random
import math
import turtle
turtle.pensize(1)
turtle.pencolor("red")
turtle.forward(100)
turtle.left(90)
turtle.mainloop()

# 🟡Day002

# 学习了数据类型
"""
python的数据类型有
1. 数值
2. 字符串
3. 布尔 
"""
a = 3.14159
b = 'abc'
d = True

# 学习了运算符
"""
运算符有
>|<|and|or|not
is|is not
"""
e = True and False
f = not e
f is True

# 学习了数据类型转换
"""
语法 type()
"""
g = 1
h = float(g)
i = str(h)

# 学习了print
"""
f字符模板，和%s
end=" "
"""
print(f"{a:.2f} 啊啊啊 {i} {g}")
print("%.2f 啊啊啊 %s %d", (a, i, g))
print("abc", end=" ")

# 学习了math库
"""
math.pi
"""
print(math.pi)

# 学习了if else
"""
if (is_a):
    xxx
elif (is_b):
    xxx
else:
    xxx
其中if的括号可以加也可以不加
"""

# 🟡Day003

# 学习了 ==
a = "abc"
b = "acb"
if a == b:
    print("{a}=={b}")

# 学习了random
"""
randint(1,10) 会随机1,2,3,4,5,5,6,7,8,9,10 包括10哦
"""
random.randint(1, 10)

# 🟡Day004

# 学习了range
"""
range(a,b)    // [a.b)
range(a,b,c)  // [a,b) 按照c跳着取，c可以是负数，a比b大时候，会倒着出值 
"""
for i in range(10):
    print(i)


# 🟡Day005

# 学习了函数
def f(n):
    if n < 2:
        return 1
    else:
        return f(n-1) + f(n-2)


for i in range(1, 11):
    print(f(i), end=" ")


# 🟡Day006

# 学习了参数
"""
def sum(*args) # 列表
def sum(**dict) # 字典
"""


def sum(*args):
    total = 0
    for i in args:
        total += i

    return total


# 学习了模块
"""
import module1 as m1 # 导入时会执行那个模块的代码
如果不想执行，在module1使用
if __name__ == "__main__" 因为导入的模块名称不会是main，当前执行的模块才是main
所以就不执行了

导入会在当前文件目录下找那个module
"""


# 🟡Day007
# 学习了字典
"""
# 创建字典
d = {"a":1,"b":2,"c":3}
# 遍历字典
for k,v in d.items():
    print("{k}:{v}")
# 更新元素
d["a"] = 0
# 添加元素
d["d"] = 4
# 删除元素(关键字)
del d["d"]
# 删除并返回value
d.delete("d")
# 弹出最后一个键值对
d.popitem()
# 判断是否存在key
if "a" in d:
    print(True)
# 清空字典
d.clear()
"""

# 学习str
"""
s = "Hello World!"
# 计算字符串的长度
len(s)
# 获得字符串首字母大写的拷贝
s.capitalize()
# 获得字符串变大写后的拷贝
s.upper()
# 从字符串中查找子串所在位置
s.find("Wor")
# 与find类似但找不到子串时会引发异常
s.index("Wor")
# 检查字符串是否以指定的字符串开头
s.startswith("H")
# 检查字符串是否以指定的字符串结尾
s.endswith("World!")
# 将字符串以指定的宽度居中并在两侧填充指定的字符
s.center(50, "*")
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
s.rjust(50,"-")
# 从字符串中取出指定位置的字符(下标运算)
s.index(10)
# 字符串切片(从指定的开始索引到指定的结束索引)
s[1:-1]
s[:]
s[3:]
s[1:-1:2]
# 检查字符串是否由数字构成
s.isdigit()
# 检查字符串是否以字母构成
s.isalpha()
# 检查字符串是否以数字和字母构成
s.isalnum()
# 获得字符串修剪左右两侧空格的拷贝
s.strip()
"""
# 学习了set
"""
# 创建集合
s = {1,2,3}
# 集合长度
len(s)
# 添加元素
s.add(4)
# 删除元素
s.remove(4)
# 检查元素
if 3 in s:
# 遍历集合
for i in s:
# 元组转集合
t = (1,2,3)
a = set(t)
# 交集
s1 = set(range(1,4))
s2 = (2,3,4)
s3 = s1 & s2
# 并集
s3 = s1 | s2
# 差集
s3 = s1 - s2
# xor
s3 = s1 ^ s2
# 是否是子集
s2 <= s3:
"""
# 学习了list
"""
l = [1,2,3,4]
# 计算列表长度(元素个数)
len(l)
# 下标(索引)运算
l[1]
# 追加元素
l.append(5)
# 在指定位置插入元素
l.insert(1,6)
# 删除元素
l.remove(6)
# 清空列表元素
l.clear()
# 切片
l[:]
# 排序
sorted(l)
sorted(l).reverse()
# 动态生成列表
[i for i in range(1,10) if i % 2 == 0]
# 斐波那契数列 yield 版本
def f(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
        yield a

for i in fib(10):
    print(i, end=" ")
"""
# 学习了tuple
"""
# 定义元组
a = (1,2,3)
# 获取元组元素
a[1]
# 遍历元组元素
for i in a:
# 元组转列表
list(a)
# 列表转元组
tuple(t)
"""
# 学习了验证码的生成
"""
captcha 验证码
"""
image = ImageCaptcha(width=200, height=100)
image.write("abc123", './captcha.png')

# 学习了rich
"""
有颜色的输出
"""
c = Console()
c.print("[red]Hello World![/red]")


# 🟡Day008

# 学习了time
time.sleep(1)

# 学习了class


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property.setter
    def x(self, value):
        self._y = value


p = Point(100, 100)
print(p.x)
p.x = 50


class Week(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


class Person(ABC):

    @abstractmethod
    def say():
        pass


# 🟡Day009

# 学习了装饰器
def simple_decorator(func):
    def warpper(func):
        print("执行前")
        func()
        print("执行后")

    return warpper


@simple_decorator
def say_hello():
    print("Hello!")


"""
等价于
say_hello = simple_decorator(say_hello)
"""

"""
带参数的函数
"""
def decorator_with_args(func):
    def warpper(*args, **kwargs):
        print(f"调用函数{func.__name__}")
        print(f"参数{args}{kwargs}")
        result = func(*args, **kwargs)
        return result

    return warpper

@decorator_with_args
def add(a, b):
    return a+b



"""
带参数的装饰器
"""
def repeat(n):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"第{i+1}次执行")
                result = func(*args, **kwargs)

            return result
        return wrapper
    return actual_decorator

