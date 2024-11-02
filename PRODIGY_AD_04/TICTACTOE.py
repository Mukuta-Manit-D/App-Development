import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # Create buttons for each cell
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.play_turn(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Reset button
        reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def play_turn(self, row, col):
        if not self.buttons[row][col]["text"] and not self.check_winner():
            # Place symbol and update board
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player
            
            # Check for win or draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))
    
    def reset_game(self):
        # Reset board and button texts
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
