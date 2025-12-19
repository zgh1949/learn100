# reportlab 
# - 原生PDF生成，提供底层Canvas API和高级Platypus流式布局引擎	
# - 功能极致强大，对PDF的每一个细节都有极高的控制力，能生成非常专业的报告

# pip install reportlab
# pip install reportlab[full] 全功能版本

from reportlab.pdfbase import pdfmetrics # pdfmetrics: 字体注册和映射
from reportlab.pdfbase.ttfonts import TTFont #  TrueType字体(TrueType的含义是：一种矢量字体，字体文件的扩展名是.ttf)
from reportlab.lib.fonts import addMapping # 字体映射: 字体名称, 字体样式, 字体索引, 字体名称

# 注册中文字体
pdfmetrics.registerFont(TTFont('SimSun', 'simsun.ttf'))  # 宋体
pdfmetrics.registerFont(TTFont('SimHei', 'simhei.ttf'))  # 黑体
pdfmetrics.registerFont(TTFont('MicrosoftYaHei', 'msyh.ttf'))  # 微软雅黑

# 设置字体映射
addMapping('SimSun', 0, 0, 'SimSun')  # 正常字体
addMapping('SimHei', 0, 1, 'SimHei')  # 粗体