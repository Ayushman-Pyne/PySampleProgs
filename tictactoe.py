import tkinter as tk
from tkinter import messagebox as mb



global game_active
global current_player
def button_click(row, col):
    global current_player, game_active
    if board[row][col] == "" and game_active:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        winner = check_winner()
        if winner:
            print("Win")
            mb.showinfo("Game Over", f"Player {winner} wins!")
            game_active = False
        elif all(board[i][j] !="" for i in range(3) for j in range(3)):
            print("Tie")
            mb.showinfo("Game Over", f"It is a Tie!")
            game_active = False
        else:
            print("switch")
            print(current_player)            
            switch_player()
            print(current_player)
            
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            print(i, j)
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[i][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    
def restart_game():
    global game_active, current_player
    game_active =True
    current_player = "X"
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            buttons[i][j].config(text="")

gui = tk.Tk()
gui.title("Tic-Tac-Toe")

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_active= True


buttons= [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(gui, text="", width=10, height=3, font=("Arial", 24), command= lambda i=i, j=j: button_click(i,j))
        buttons[i][j].grid(row=i, column=j)
        

restart_button = tk.Button(gui, text="Restart", font=("Arial", 14), command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

gui.mainloop()