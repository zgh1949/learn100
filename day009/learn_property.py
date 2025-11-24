# @property的作用
# 1. 把方法调用转换成属性访问
class Person:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return self._first_name + self._last_name

    @property
    def full_name(self):
        return self._first_name + self._last_name


p = Person("z", "gh")
print(p.get_full_name())   # 传统的方法调用
print(p.full_name)         # 方法调用变成了属性访问


# 2. 变成属性后可以配合setter来进行赋值校验
class Study:
    def __init__(self, name, score):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("小于0")
        elif score > 100:
            raise ValueError("大于100")
        else:
            self._score = score


a = Study("zgh", 0)
a.score = 100
print(a.score)
# a.score = 200 # Error


# 描述符基础协议
## 描述符协议控制属性的访问机制
## 用__get__控制属性的获取
## 用__set__控制属性的设置
## 用__del__控制属性的删除


# 手动实现@propery
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        """描述符协议：get在属性方式时调用"""
        print("__get__")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("属性不可读")
        return self.fget(obj)

    def __set__(self, obj, value):
        """描述符协议：set在属性赋值时调用"""
        print("__set__")
        if self.fset is None:
            raise AttributeError("属性不可写")
        self.fset(obj, value)

    def __delete__(self, obj):
        """描述符协议：delete在属性删除时调用"""
        print("__del__")
        if self.fdel is None:
            raise AttributeError("属性不可删除")
        self.fdel(obj)

    def getter(self, fget):
        """创建新的 MyProperty，更新 getter 方法"""
        # 返回新实例，保持其他方法不变
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        """创建新的 MyProperty，更新 setter 方法"""
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        """创建新的 MyProperty，更新 deleter 方法"""
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

    def __repr__(self):
        """友好的字符串表示"""
        return f"<MyProperty object at {hex(id(self))}>"

# 使用
class Sphere:
    def __init__(self, radius):
        self._radius = radius

    @MyProperty
    def radius(self):
        """球的半径"""
        print("获取半径")
        return self._radius

    """
        上面的代码等价于
        def radius(self):  # 原始方法
            return self._radius
        radius = MyProperty(radius)  # radius()以fget传入
        # radius变量是一个MyProperty实例，这个实例实现了描述符协议可以 获取、= 赋值、del等操作
    """

    @radius.setter
    def radius(self, value):
        """设置球的半径，带验证"""
        print("设置半径")
        if value <= 0:
            raise ValueError("半径必须为正数")
        self._radius = value

    """
        上面的代码等价于
        def setter_method(self, value):  # 新的setter方法
            self._radius = value
        radius = radius.setter(setter_method)   # radius以fset传入
    """

    @radius.deleter
    def radius(self):
        """删除半径"""
        print("删除半径")
        del self._radius

    @MyProperty
    def volume(self):
        """球的体积（计算属性）"""
        import math
        return (4/3) * math.pi * (self.radius ** 3)

s = Sphere(5)
print(f"半径: {s.radius}")
print(f"体积: {s.volume:.2f}")

