from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_formatted_document(filename="day027/report.pdf"):
    # 创建文档模板
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # 获取样式
    styles = getSampleStyleSheet()
    
    # 创建自定义样式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#003366'),
        spaceAfter=30
    )
    
    # 构建文档内容
    story = []
    
    # 1. 标题
    story.append(Paragraph("月度销售报告", title_style))
    story.append(Spacer(1, 20))
    
    # 2. 子标题
    story.append(Paragraph("2024年1月", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    # 3. 段落
    text = """本报告总结了2024年1月的销售情况。总体表现良好，
    销售额同比增长15%。主要增长来自电商渠道，同比增长25%。"""
    story.append(Paragraph(text, styles["Normal"]))
    story.append(Spacer(1, 20))
    
    # 4. 表格
    data = [
        ['产品', '数量', '销售额(元)', '同比增长'],
        ['智能手机', '1,200', '3,600,000', '+20%'],
        ['笔记本电脑', '800', '4,000,000', '+15%'],
        ['平板电脑', '1,500', '3,000,000', '+30%'],
        ['配件', '5,000', '1,000,000', '+10%']
    ]
    
    # 创建表格
    table = Table(data, colWidths=[2*inch, 1.5*inch, 2*inch, 1.5*inch])
    
    # 设置表格样式
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F81BD')),  # 表头背景
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # 表头文字颜色
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 居中对齐
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # 表头字体
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # 表头字号
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # 表头底部间距
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # 数据行背景
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),  # 网格线
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),  # 斑马纹
    ]))
    
    story.append(table)
    story.append(Spacer(1, 30))
    
    # 5. 列表
    story.append(Paragraph("下月重点工作:", styles['Heading3']))
    
    bullet_points = [
        "扩大线上营销渠道",
        "优化库存管理",
        "开发新产品线",
        "客户满意度调查"
    ]
    
    for point in bullet_points:
        story.append(Paragraph(f"• {point}", styles["Bullet"]))
    
    # 构建文档
    doc.build(story)

create_formatted_document()