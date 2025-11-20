def sum(*args):
    sum_of_all = 0
    for i in args:
        sum_of_all += i

    return sum_of_all

print(sum(1,2,3,4,5,6,7))


def foo():
    print(a)  # 闭包可以访问 外层的变量 100
    # a = 200 # 如果重新定义一个a，那就无法访问外部的，而是使用新定义的
    # print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
