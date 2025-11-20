# 创建字典
d = {"a": 1, "b": 2, "c": 3}

# 遍历字典
def print_dict(d):
    print("___")
    for k,v in d.items():
        print(f"{k}={v}")
    print("___")

print_dict(d)

# 更新元素
d["a"] = 4
print("更新元素a")
print_dict(d)

# 添加元素
d["d"]=5
print("添加元素d")
print_dict(d)

# 删除元素(关键字)
del d["d"]
print("删除元素d")

# 删除并返回value
print_dict(d)
print("删除元素b")
print(d.pop("b")) 

# 弹出最后一个键值对
print("弹出最后一个键值对")
print(d.popitem()) 
print("___")

# 判断是否存在key
print("现在d是否存在")
if "d" in d:
    print("存在")
else:
    print("不存在")

# 清空字典
print("清空字典")
d.clear()
print(d)