# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random

code_char = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_code(n):
    return ''.join(random.sample(code_char, n))

for _ in range(10):
    print(generate_code(6))


# 扩展：生成验证码图片
from captcha.image import ImageCaptcha
import random
import string

def generate_random_text(length=4):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

## 创建验证码
image = ImageCaptcha(width=200, height=100)

code = generate_random_text(6)

image.write(code, './day007/captcha.png')

print("生成验证码:", code)
