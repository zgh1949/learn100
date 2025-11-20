# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

## 自定义数据结构，类似列表，但只保留最大的n个
class OnlyTop:
    def __init__(self, n):
        self.capacity = n
        self.data = []

    def put(self, value):
        # 如果列表有空位，就追加进去
        if len(self.data) < self.capacity:
            self.data.append(value)
        else:
            min_value = min(self.data)
            min_index = self.data.index(min_value)
            if (value > min_value):
                del self.data[min_index]
                self.data.insert(min_index, value)

    def get(self):
        return self.data


## 寻找top2
def get_top2(l):
    if (len(l) < 1):
        return ()
    elif (len(l) == 1):
        return (l[0], l[0])
    elif (len(l) == 2):
        return (l[0], l[1]) if l[0] >= l[1] else (l[1], l[0])
    else:
        only_top = OnlyTop(2)
        for i in l:
            only_top.put(i)
        return only_top.get()

l = [1,4,6,4,7,8,3,6,8,9,3,7,9,0]
print(get_top2(l))