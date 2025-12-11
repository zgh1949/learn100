"""
Python的异常和Java差不多

BaseException所有异常的基类
- SystemExit 解释器请求退出
- KeyboardInterrupt 用户中断程序执行
- GeneratorExit 生成器发生异常通知
- Exception 常规异常的父类

raise 抛出异常
"""

# try
file = None
try:
    file = open('day001/abc.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读文件时解码错误！')
finally:
    if file:
        file.close()


# 自定义异常
class InputError(ValueError):
    """自定义异常"""
    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        raise InputError('非负数无法阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num-1)


try:
    print(fac(5))
except IndexError as err:
    print(err)

# with
try:
    with open('day011/abc.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读文件时解码错误！')

# 读写二进制
try:
    with open('day011/python-logo.png', 'rb') as file1:
        data = file1.read()
except FileNotFoundError:
    print('文件无法被打开')
except IOError:
    print('读写文件时出错！')

# 如果文件很大
try:
    with open('day011/python-logo.png', 'rb') as file1, open('day011/python-logo-copy.png', 'wb') as file2:
        data = file1.read(10240) # 一次读取10KB
        while data:
            print("复制中")
            file2.write(data)
            data = file1.read(10240)
except FileNotFoundError:
    print("无法打开指定文件")
except IOError:
    print("读写文件出错")

print("复制完毕")


# 不要使用异常机制来处理正常的业务逻辑或者控制程序