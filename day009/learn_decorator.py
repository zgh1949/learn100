# 学习装饰器的基本原理

# A.简单的装饰器
# : 给一个函数，返回一个被装饰的函数
# ! 装饰器针对的函数，返回的也是函数，装饰的过程没有执行目标函数
def simple_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

"""
    上面等价于
    def say_hello():
        print("Hello!")
    say_hello = simple_decorator(say_hello) # say_hello变成了装饰器实例，是warpper了
"""

# B.带参数的函数
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数:{func.__name__}")
        print(f"参数：{args},{kwargs}")
        result = func(*args, **kwargs)
        print("函数执行完毕")
        return result

    return wrapper


@decorator_with_args
def add(a, b):
    return a+b


@decorator_with_args
def greet(name, message="你好"):
    return f"{message}, {name}!"


print(add(3, 4))
print(greet("Alice", message="Hello"))


# C.带参数的装饰器
## 第一层：接收装饰器参数
def repeat(n):
    ## 第二层：接收被装饰的函数
    def actual_decorator(func):
        ## 第三层：接收被装饰的函数的参数
        def wrapper(*args, **kwargs):
            ## 跟进前几层得到的信息进行装饰
            for i in range(n):
                print(f"第{i+1}次执行:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat(3)
def print_hello(name="World"):
    print(f"Hello {name}!")

print_hello(name="zgh")


# D. @functools.wraps(func)
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def example():
    """示例函数"""
    pass

print(example.__name__)  # 输出: wrapper（不是我们想要的）
print(example.__doc__)   # 输出: None（文档字符串丢失了）

import functools

def my_decorator(func):
    @functools.wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        """包装函数的文档字符串"""
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print("函数执行完毕")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """打招呼函数"""
    print(f"Hello, {name}!")
    return f"已向 {name} 打招呼"

# 测试
print(say_hello.__name__)  # 输出: say_hello（而不是 wrapper）
print(say_hello.__doc__)   # 输出: 打招呼函数（而不是包装函数的文档字符串）
say_hello("Alice")