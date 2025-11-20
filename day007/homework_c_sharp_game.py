import tkinter as tk
from tkinter import messagebox

class SimpleTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("井字棋")
        self.window.resizable(False, False)
        
        # 游戏状态
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # 创建界面
        self.create_board()
        self.create_restart_button()
    
    def create_board(self):
        """创建游戏棋盘"""
        self.buttons = []
        
        for i in range(3):
            row = []
            for j in range(3):
                index = i * 3 + j
                btn = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 20),
                    width=4,
                    height=2,
                    command=lambda idx=index: self.make_move(idx)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)
    
    def create_restart_button(self):
        """创建重新开始按钮"""
        restart_btn = tk.Button(
            self.window,
            text="重新开始",
            font=("Arial", 12),
            command=self.reset_game
        )
        restart_btn.grid(row=3, column=0, columnspan=3, pady=10)
    
    def make_move(self, position):
        """玩家落子"""
        if self.game_over or self.board[position] != "":
            return
        
        # 更新棋盘
        self.board[position] = self.current_player
        row, col = position // 3, position % 3
        self.buttons[row][col].config(text=self.current_player, state="disabled")
        
        # 检查游戏状态
        if self.check_winner():
            self.game_over = True
            messagebox.showinfo("游戏结束", f"{self.current_player} 获胜!")
        elif self.is_board_full():
            self.game_over = True
            messagebox.showinfo("游戏结束", "平局!")
        else:
            # 切换玩家
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        """检查是否有玩家获胜"""
        # 检查行
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
        
        # 检查列
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        
        # 检查对角线
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        
        return False
    
    def is_board_full(self):
        """检查棋盘是否已满"""
        return "" not in self.board
    
    def reset_game(self):
        """重置游戏"""
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False
        
        # 重置按钮
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
    
    def run(self):
        """运行游戏"""
        self.window.mainloop()

# 创建并运行游戏
if __name__ == "__main__":
    game = SimpleTicTacToe()
    game.run()