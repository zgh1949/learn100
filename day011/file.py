"""
r 读
w 写
x 写，文件存在报异常
a 追加
b 二进制
t 文本模式（默认，可以通过encoding来指定编码）
+ 更新（可读可写）
"""
# 读
file = open('day011/abc.txt', "r", encoding='utf-8')
print(file.read())
file.close()
# 写
file = open('day011/abc.txt', 'a', encoding="utf-8")
file.write("\n添加的文字")
file.close()
# 读
file = open('day011/abc.txt', encoding='utf-8')
for line in file.readlines():
    print(line, end='')
file.close()
