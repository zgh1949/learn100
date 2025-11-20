import time
import random
import sys
import os

def get_terminal_size():
    """获取终端窗口尺寸"""
    if sys.platform == "win32":
        # Windows特定方法
        import ctypes
        from ctypes import wintypes
        
        # 定义控制台屏幕缓冲区信息结构
        class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
            _fields_ = [
                ("dwSize", wintypes._COORD),
                ("dwCursorPosition", wintypes._COORD),
                ("wAttributes", wintypes.WORD),
                ("srWindow", wintypes.SMALL_RECT),
                ("dwMaximumWindowSize", wintypes._COORD),
            ]
        
        # 获取标准输出句柄
        h_stdout = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        
        # 获取控制台屏幕缓冲区信息
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h_stdout, ctypes.byref(csbi))
        
        # 计算窗口尺寸
        columns = csbi.srWindow.Right - csbi.srWindow.Left + 1
        rows = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        
        return rows, columns
    else:
        # Unix/Linux方法
        try:
            import termios
            import struct
            import fcntl
            s = struct.pack('HHHH', 0, 0, 0, 0)
            x = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s)
            return struct.unpack('HHHH', x)[0], struct.unpack('HHHH', x)[1]
        except:
            # 如果获取失败，使用默认值
            return 24, 80

def draw_dance_text(center_x, center_y):
    """绘制ASCII艺术字'Dance!'"""
    # ASCII艺术字
    dance_art = [
        " ____                                ",
        "|  _ \    __ _   _ __     ___    ___ ",
        "| | | |  / _` | | '_ \   / __|  / _ \\",
        "| |_| | | (_| | | | | | | (__  |  __/",
        "|____/   \__,_| |_| |_|  \___|  \___|",
    ]
    
    # 计算起始位置
    start_x = center_x - len(dance_art[0]) // 2
    start_y = center_y - len(dance_art) // 2
    
    # 绘制艺术字
    for i, line in enumerate(dance_art):
        for j, char in enumerate(line):
            if char != ' ':
                # 使用彩虹色
                color = 31 + (i + j) % 7  # 31-37是基本颜色
                print(f'\033[{start_y+i};{start_x+j}H\033[{color}m{char}\033[0m', end='')

def dance_cursor():
    # 启用Windows的ANSI支持
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # 启用虚拟终端处理
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    
    # 获取终端尺寸
    try:
        rows, columns = get_terminal_size()
    except:
        rows, columns = 24, 80  # 如果获取失败使用默认值
    
    # 隐藏光标
    print('\033[?25l', end='')
    
    # 扩展的跳舞字符集合 - 增加更多花里胡哨的字符
    dancers = ['♠', '♣', '♥', '♦', '♪', '♫', '☼', '★', '☆', '◆', '◇', '○', '●', '□', '■', '△', '▽', '◁', '▷', '◀', '▶']
    colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]  # 扩展颜色范围
    
    try:
        # 存储所有舞者的位置
        positions = []
        # 增加舞者数量
        for _ in range(20):
            positions.append({
                'x': random.randint(1, columns-2),
                'y': random.randint(1, rows-2),
                'dx': random.choice([-1, 1]),
                'dy': random.choice([-1, 1]),
                'char': random.choice(dancers),
                'color': random.choice(colors),
                'trail': []  # 添加轨迹
            })
        
        # 跳舞循环 - 增加循环次数
        for step in range(5000):
            # 清屏
            print('\033[2J\033[H', end='')
            
            # 绘制"Dance!"艺术字
            draw_dance_text(columns // 2, rows // 2)
            
            # 更新并绘制每个舞者
            for pos in positions:
                # 边界检测和反弹
                if pos['x'] <= 1 or pos['x'] >= columns-2:
                    pos['dx'] *= -1
                    # 碰到边界时改变颜色
                    pos['color'] = random.choice(colors)
                if pos['y'] <= 1 or pos['y'] >= rows-2:
                    pos['dy'] *= -1
                    # 碰到边界时改变颜色
                    pos['color'] = random.choice(colors)
                
                # 更新位置
                pos['x'] += pos['dx']
                pos['y'] += pos['dy']
                
                # 添加到轨迹
                pos['trail'].append((pos['x'], pos['y']))
                # 限制轨迹长度
                if len(pos['trail']) > 5:
                    pos['trail'].pop(0)
                
                # 绘制轨迹
                for i, (tx, ty) in enumerate(pos['trail']):
                    # 轨迹颜色逐渐变淡
                    trail_color = pos['color'] if i == len(pos['trail']) - 1 else 90
                    print(f'\033[{ty};{tx}H\033[{trail_color}m·\033[0m', end='')
                
                # 随机改变方向（增加随机性）
                if random.random() < 0.1:
                    pos['dx'] = random.choice([-1, 1])
                if random.random() < 0.1:
                    pos['dy'] = random.choice([-1, 1])
                
                # 随机改变舞者
                if random.random() < 0.05:
                    pos['char'] = random.choice(dancers)
                
                # 随机改变颜色
                if random.random() < 0.05:
                    pos['color'] = random.choice(colors)
                
                # 设置颜色并绘制
                print(f'\033[{pos["y"]};{pos["x"]}H\033[{pos["color"]}m{pos["char"]}\033[0m', end='')
            
            # 在底部显示说明 - 取消步骤显示
            sys.stdout.flush()
            
            # 减少延迟，使动画更流畅
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        pass
    finally:
        # 恢复光标显示
        print('\033[?25h', end='')
        # 清屏并重置
        print('\033[2J\033[H\033[0m', end='')
        print("舞蹈结束！")

if __name__ == "__main__":
    dance_cursor()