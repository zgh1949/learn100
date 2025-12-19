from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

class ReportWithHeaderFooter(SimpleDocTemplate):
    """自定义文档模板，添加页眉页脚"""
    
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        self.page_number = 0
        
    def onFirstPage(self, canvas, doc):
        self.page_number += 1
        self._create_header_footer(canvas, doc, is_first_page=True)
        
    def onLaterPages(self, canvas, doc):
        self.page_number += 1
        self._create_header_footer(canvas, doc, is_first_page=False)
        
    def _create_header_footer(self, canvas, doc, is_first_page):
        # 保存当前状态
        canvas.saveState()
        
        # 页眉
        canvas.setFont('Helvetica', 10)
        canvas.drawString(doc.leftMargin, doc.height + doc.topMargin + 0.5*cm, 
                         "公司机密 - 严禁外传")
        
        # 页脚
        canvas.setFont('Helvetica', 9)
        page_text = f"第 {self.page_number} 页"
        canvas.drawCentredString(doc.width/2 + doc.leftMargin, 1*cm, page_text)
        
        # 公司信息
        canvas.drawRightString(doc.width + doc.leftMargin, 1*cm, "ABC有限公司")
        
        # 恢复状态
        canvas.restoreState()

def create_complex_report():
    """创建包含多页、图表、表格的复杂报告"""
    filename = "day027/complex_report.pdf"
    doc = ReportWithHeaderFooter(
        filename,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=3*cm,  # 为页眉留出空间
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    # 第一章
    story.append(Paragraph("第一章：执行摘要", styles['Heading1']))
    story.append(Spacer(1, 12))
    
    # 添加一些示例内容
    for i in range(20):
        story.append(Paragraph(f"这是第{i+1}个段落的内容。" * 5, styles['Normal']))
        story.append(Spacer(1, 6))
    
    # 分页
    story.append(PageBreak())
    
    # 第二章
    story.append(Paragraph("第二章：详细分析", styles['Heading1']))
    
    # 复杂表格示例
    story.append(Spacer(1, 20))
    story.append(Paragraph("销售数据季度对比", styles['Heading2']))
    
    # 创建季度数据表格
    quarterly_data = [
        ['季度', 'Q1', 'Q2', 'Q3', 'Q4', '总计'],
        ['2023年', '1,200', '1,500', '1,800', '2,000', '6,500'],
        ['2024年', '1,500', '1,800', '2,100', '2,400', '7,800'],
        ['同比增长', '+25%', '+20%', '+17%', '+20%', '+20%']
    ]
    
    from reportlab.platypus import Table, TableStyle
    
    table = Table(quarterly_data, colWidths=[2*cm, 2*cm, 2*cm, 2*cm, 2*cm, 2*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E5894')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#E6F3FF')),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#FFE6E6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(table)
    
    # 构建文档
    doc.build(story)
    print(f"PDF已生成: {filename}")

create_complex_report()