import xlrd
import xlwt
from xlutils.copy import copy

wb_for_read = xlrd.open_workbook('day024/考试成绩表.xls')
sheet1 = wb_for_read.sheet_by_index(0)
nrows, ncols = sheet1.nrows, sheet1.ncols

wb_for_write = copy(wb_for_read)

sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows, 2, xlwt.Formula(f'average(B2:B{nrows})'))
sheet2.write(nrows, 3, xlwt.Formula(f'sum(B2:G{nrows})'))
wb_for_write.save('day024/考试成绩表2.xls')