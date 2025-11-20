# 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(name):
    index = name.find('.')
    return name[index+1:]


names = ['smo_file.tar.gz', 'x007.png']
for name in names:
    suffix = get_suffix(name)
    print(f"{name} 的后缀名称是 {suffix}")
