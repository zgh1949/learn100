from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import inch, cm

def create_simple_pdf(filename="day027/simple.pdf"):
    # 创建Canvas对象
    c = canvas.Canvas(filename, pagesize=A4)
    
    # 设置文档标题
    c.setTitle("我的第一个PDF")
    
    # 设置字体和大小
    c.setFont("Helvetica", 12)
    
    # 绘制文本
    c.drawString(100, 800, "Hello, ReportLab!")  # 坐标 (x, y)
    
    # 设置字体颜色
    c.setFillColorRGB(1, 0, 0)  # 红色
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "这是红色加粗文本")
    
    # 画线
    c.setStrokeColorRGB(0, 0, 1)  # 蓝色
    c.line(100, 740, 400, 740)  # 从(100,740)到(400,740)
    
    # 画矩形
    c.setFillColorRGB(0.9, 0.9, 0.9)  # 浅灰色填充
    c.rect(100, 650, 200, 50, fill=1)  # 填充矩形
    
    # 画圆
    c.setFillColorRGB(0, 1, 0)  # 绿色
    c.circle(300, 600, 30, fill=1)  # 圆心(300,600)，半径30
    
    # 添加图片
    c.drawImage("day027/python-logo.png", 100, 500, width=100, height=50)
    
    # 保存PDF
    c.save()

create_simple_pdf()