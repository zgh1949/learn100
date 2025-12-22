# pip install pillow

from PIL import Image, ImageFilter

img = Image.open('day028/python-logo.png')
print(img.format)
print(img.size)
print(img.mode)  # 图像模式
img.show()

# 裁剪图像
img.crop((8, 8, 300, 300)).show()

# 生成缩略图
img.thumbnail((128, 128))
img.show()

# 缩放和贴图
gopher = Image.open('day028/gopher.png')
logo = Image.open('day028/python-logo.png')

logo_crop = logo.crop((8, 8, 320, 350))
width, height = logo_crop.size
logo_resize = logo_crop.resize((int(width/10), int(height/10)))

gopher.paste(logo_resize, (430, 170))
gopher.show()


# 旋转和翻转
logo = Image.open('day028/gopher.png')
logo.rotate(45).show()
logo.transpose(Image.FILTERED).show()

# 操作像素
for x in range(80, 100):
    for y in range(80, 100):
        logo.putpixel((x, y), (128, 128, 128))
logo.show()


# 滤镜
logo.filter(ImageFilter.CONTOUR).show()