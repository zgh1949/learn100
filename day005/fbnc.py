# 斐波那契数列
def f(n):
    if(n<=2):
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input("n="))
for i in range(1, n + 1):
    print(f(i), end=" ")