# 创建集合
s = {1, 2, 3}
s = set(range(1, 11))
# 集合长度
print(len(s))
# 添加元素
s.add(11)
s.add(11)  # 重复添加只保存一个
print(s)
# 删除元素
s.remove(11)
# 检查元素
print(3 in s)
# 遍历集合
for i in s:
    print(i, end="")
print()
# 元组转集合
l = list(s)
# 交集
s1 = set(range(5, 16))
print(s & s1)
# 并集
print(s | s1)
# 差集
print(s - s1)
# xor
print(s ^ s1)
# 是否是子集
s3 = {7, 8, 9}
print(s1 <= s)
print(s3 <= s)