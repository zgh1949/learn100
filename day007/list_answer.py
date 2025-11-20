list1 = [1, 3, 5, 7, 100]

# 计算列表长度(元素个数)
print(len(list1))
# 下标(索引)运算
print(list1[1])
# 追加元素
list1.append(200)
print(list1)
# 在指定位置插入元素
list1.insert(1, 2)
print(list1)
# 删除元素
list1.remove(1)
print(list1)
# 切片
list2 = list1[::2]
# 排序
sorted(list1).reverse()
print(list1)
# 动态生成列表
leap_year = [x for x in range(1, 2040) if (
    x % 4 == 0 and x % 100 != 0) or x % 400 == 0]
for i in leap_year:
    print("闰年：", i)
# 斐波那契数列 yield 版本
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
        yield a

for i in fib(10):
    print(i, end=" ")
print()

# 清空列表元素
list1.clear()
print(list1)
