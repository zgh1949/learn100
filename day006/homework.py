# 实现计算求最大公约数和最小公倍数的函数。
def calcualte(a, b):
    small, big = sorted([a, b])
    x = 0
    while True:
        c = big % small
        big = small
        small = c
        if (c == 0):
            x = big
            break
    y = int(a * b / x)
    return (x, y)


a = 8
b = 12

print(f"{a} {b} 的最大公约数与最小公倍数是", calcualte(8, 12))

print()

# 练习2：实现判断一个数是不是回文数的函数。
def check_palindrome(num):
    num_array = list(str(num))
    num_array_length = len(num_array)
    for i in range(int(num_array_length / 2)+1):
        if num_array[i] != num_array[num_array_length - 1 - i]:
            return False
    return True


def print_check_palindrome(n):
    print(f"{n} {'是' if check_palindrome(n) else '不是'}回文数")

print_check_palindrome(1)
print_check_palindrome(12)
print_check_palindrome(123)
print_check_palindrome(1232)
print_check_palindrome(12321)

print()

# 练习3：实现判断一个数是不是素数的函数。


def check_prime_number(num):
    for i in range(2, int(num / 2) + 1):
        if (num % i == 0):
            return False
    return True


def print_check_prime_number(num):
    print(f"{num} {'是' if check_prime_number(num) else '不是'} 素数")

for i in range(2,14):
    print_check_prime_number(i)

print()


# 练习4：写一个程序判断输入的正整数是不是回文素数。
def double_check(num):
    return check_palindrome(num) and check_prime_number(num)

def print_double_check(num):
    if(double_check(num)):
        print(f"{num} 是回文素数")

## 找出10000内回文素数
for i in range(2, 10000):
    print_double_check(i)




