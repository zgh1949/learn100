# 处理老版本的excel常用xl系列
# xlwt 写
# xlrd 读

# 安装命令
# pip install xlwt xlrd xlutils
import xlrd

# open_workbook
wb = xlrd.open_workbook('day024/test.xls')

# wb.sheet_names
for sheetname in wb.sheet_names():
    print(sheetname)

# wb.sheet_by_name
sheet = wb.sheet_by_name(wb.sheet_names()[0])
print(sheet.nrows, sheet.ncols)

# 遍历
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell = sheet.cell(row, col)
        value = cell.value
        print(f"{row+1}行,{col+1}列——>{value}")

# cell_type : 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(f"last cell type is:{last_cell_type}")

# row_values(row)
print(sheet.row_values(0))

# row_slise(row, start_index, end_index)
print(sheet.row_slice(3, 0, 5)) 
