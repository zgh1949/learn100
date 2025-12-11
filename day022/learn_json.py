import json

my_dict = {
    'name': 'zgh',
    'age': 29,
    'friends': None,
    'cars': None,
    'games': [
        {'name': '黑神话悟空', 'type': '动作冒险'},
        {'name': '艾尔登法环', 'type': '动作冒险'},
        {'name': '荒野大镖客2', 'type': '骑马模拟'}
    ]
}



"""
dump ——> 转储

dump 转储到文件
dumps 转储到str

带s的string, 除了json之外的工具也是这个道理
"""

# dumps
print(json.dumps(my_dict))

# dump
with open("day012/json.txt", "w", encoding="utf-8") as file1:
    json.dump(my_dict, file1)


"""
load：从文件（或文件类对象）中读取数据，并将其反序列化为Python对象。
loads：从字符串（string）中读取数据，并将其反序列化为Python对象。
"""
# load
with open("day012/json.txt", "r", encoding="utf-8") as file2:
    print(json.load(file2))
