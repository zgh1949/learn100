import random
import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]

# 创建wb对象
wb = xlwt.Workbook()

sheet = wb.add_sheet("一年级")

# 样式对象
header_style = xlwt.XFStyle()

# 填充
pattern = xlwt.Pattern() # 背景填充对象
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # 填充方式，实心填充
pattern.pattern_fore_colour = 5  # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
header_style.pattern = pattern

# 字体
font = xlwt.Font()
font.name = '华文楷体'
font.height = 20 * 18
font.bold = True
font.italic = True
font.colour_index = 0
header_style.font = font

# 对齐
align = xlwt.Alignment()
align.vert = xlwt.Alignment.VERT_CENTER # 垂直方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER # 水平方向的对齐方式
header_style.alignment = align

# 边框
borders = xlwt.Borders()
props = (
    ('top', 'top_colour'), ('right', 'right_colour'),
    ('bottom', 'bottom_colour'), ('left', 'left_colour')
)
for position, color in props: # 通过循环对四个方向的边框样式及颜色进行设定
    setattr(borders, position, xlwt.Borders.DASHED)     # 使用setattr内置函数动态给对象指定的属性赋值
    setattr(borders, color, 5)
header_style.borders = borders

# 设置行高为40px
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
      # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    sheet.write(0, index, title, header_style)  # write(row, col, value)

for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row+1, col+1, scores[row][col])

wb.save('day024/考试成绩表.xls')
