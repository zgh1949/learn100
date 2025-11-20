import os
import time

def refresh():
    content = "北京欢迎你，为你开天辟地..."
    try:
        while True:
            # 使用ANSI转义序列 - 最快最可靠
            print('\033[2J\033[H', end='')
            print(content)
            time.sleep(0.2)
            content = content[1:] + content[0]
    except KeyboardInterrupt:
        print("\n跑马灯已停止")

if __name__ == "__main__":
    refresh()