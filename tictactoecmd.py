def update_board(row, col):
    global current_player, game_active
    if row in range(3) and col in range(3):
        if board[row][col] == " " and game_active:
            board[row][col] = current_player
            return True
        else:
            return False
    else:
        return False

def print_board():
    print(" || ".join(board[0]))
    print("===========")
    print(" || ".join(board[1]))
    print("===========")
    print(" || ".join(board[2]))


def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
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
            board[i][j] = " "


# terminal colors
RED = "\033[31m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_active= True

def main():
    game_active= True
    
    while game_active:
        print_board()
        print(f"{current_player}'s turn")
        r = int(input("Enter the row number: ")) - 1
        c = int(input("Enter the column number: ")) - 1
        if update_board(r,c):
            print("---------------------------")
        else:
            print(f"                            {RED}Wrong Input! Try again!{RESET}")
            continue

        winner = check_winner()
        if winner:
            print_board()
            print(f"                            {GREEN}{winner} Wins{RESET}")
            game_active = False
        elif all(board[i][j] !=" " for i in range(3) for j in range(3)):
            print_board()
            print(f"                             {BLUE}That's A Tie!{RESET}")
            game_active = False
        else:
            switch_player()
        



if __name__ == "__main__":
    main()