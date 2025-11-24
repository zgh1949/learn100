# 类方法

# - 类方法用@classmethod装饰
# - 类方法第一个参数是cls, 代表类本身


# 用处1：代替构造函数
## 用字符串代替数值来创建日期
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        """从'YYYY-MM-DD'格式字符串创建日期"""
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        """从时间戳创建日期"""
        # 伪代码：时间戳转换逻辑
        return cls(year, month, day)

date1 = Date(2023, 10, 1)  # 传统方式
date2 = Date.from_string("2023-10-01")  # 类方法方式

# 用处2：用于继承中的多态
class Animal:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def create_default(cls):
        """创建默认的动物实例"""
        return cls("未知动物")  # 使用当前类

class Dog(Animal):
    @classmethod
    def create_default(cls):
        """创建默认的狗实例"""
        return cls("未知品种的狗")

animal = Animal.create_default()  # Animal实例
dog = Dog.create_default()        # Dog实例（多态性保持）

## 用处2：访问或修改类变量
class Counter:
    _count = 0  # 类变量
    
    def __init__(self):
        Counter._count += 1
        self.id = Counter._count
    
    @classmethod
    def get_count(cls):
        """获取已创建的实例数量"""
        return cls._count
    
    @classmethod
    def reset_counter(cls):
        """重置计数器"""
        cls._count = 0


# 静态方法 VS 类方法
# ！需要使用类本身的时候使用类方法（如修改类变量，使用构造器）
# ！纯粹的工具函数选择静态方法