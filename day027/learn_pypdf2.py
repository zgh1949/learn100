# python操作PDF的工具多种多样，各有千秋，PyPDF2是最基础的那种

# pip install PyPDF2
import PyPDF2

# 读取原始PDF
reader = PyPDF2.PdfReader('day027/test.pdf')
for page in reader.pages:
    print(page.extract_text()) # 打印pdf内容

# 旋转pdf - 使用新的reader实例
reader1 = PyPDF2.PdfReader('day027/test.pdf')
writer1 = PyPDF2.PdfWriter()
for page in reader1.pages:
    new_page = page.rotate(-90)
    writer1.add_page(new_page)
    
with open('day027/test_edit.pdf', 'wb') as file1:
    writer1.write(file1)

# 加密pdf - 使用新的reader实例
reader2 = PyPDF2.PdfReader('day027/test.pdf')
writer2 = PyPDF2.PdfWriter()
for page in reader2.pages:
    writer2.add_page(page)

writer2.encrypt('foobared')

with open('day027/test_encrypt.pdf', 'wb') as file2:
    writer2.write(file2)

# 添加水印 - 使用新的reader实例
reader3 = PyPDF2.PdfReader('day027/test.pdf')
writer3 = PyPDF2.PdfWriter()
reader_watermark = PyPDF2.PdfReader('day027/watermark.pdf')
watermark_page = reader_watermark.pages[0]

for page in reader3.pages:
    page.merge_page(watermark_page)
    writer3.add_page(page)

with open('day027/test_with_watermark.pdf', 'wb') as file3:
    writer3.write(file3)

