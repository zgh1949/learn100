import csv
import random

# wirter writerow reader

# BUG 为什么加newline=""? Python会在每行后面添加额外的空行。这是因为CSV writer在内部使用\n作为行结束符，而Windows系统会将\n转换为\r\n，导致每行之间出现空行
with open("day023/scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=",",
                        quoting=csv.QUOTE_ALL)  # quoting 引号
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)

with open("day023/scores.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=",") # reader类似一个可迭代的二维数组
    for data_list in reader:
        print(reader.line_num, end='\t')
        for element in data_list:
            print(element, end="\t")
        print()
