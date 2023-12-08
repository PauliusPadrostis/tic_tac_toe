board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
h_line = "+---+---+---+"
v_line = "|"
spacer = "|-------------------|"


def build_board():
    print(spacer)
    for row in board[::-1]:
        print(f"\t{h_line}")
        print(f"\t{v_line} {row[0]} {v_line} {row[1]} {v_line} {row[2]} {v_line}")
    print(f"\t{h_line}")
    print(spacer)


def update_board(board, num_choice, player):
    row = -1
    for x in board:
        col = -1
        row += 1
        for xx in x:
            col += 1
            if xx == num_choice:
                board[row][col] = player
                build_board()
                break


def change_current_player():
    global current_player_sign, current_player_name
    if current_player_name == "Player1":
        current_player_name = "Player2"
        current_player_sign = "O"
    else:
        current_player_name = "Player1"
        current_player_sign = "X"


def check_horizontal(board):
    frh = [board[0][0], board[0][1], board[0][2]]
    srh = [board[1][0], board[1][1], board[1][2]]
    trh = [board[2][0], board[2][1], board[2][2]]

    if frh[0] == frh[1] == frh[2]:
        return True
    elif srh[0] == srh[1] == srh[2]:
        return True
    elif trh[0] == trh[1] == trh[2]:
        return True
    else:
        return False


def check_vertical(board):
    fcv = [board[0][0], board[1][0], board[2][0]]
    scv = [board[0][1], board[1][1], board[2][1]]
    tcv = [board[0][1], board[1][1], board[2][1]]

    if fcv[0] == fcv[1] == fcv[2]:
        return True
    elif scv[0] == scv[1] == scv[2]:
        return True
    elif tcv[0] == tcv[1] == tcv[2]:
        return True
    else:
        return False


def check_diagonal(board):
    fdia = [board[0][0], board[1][1], board[2][2]]
    sdia = [board[2][0], board[1][1], board[0][2]]

    if fdia[0] == fdia[1] == fdia[2]:
        return True
    elif sdia[0] == sdia[1] == sdia[2]:
        return True
    else:
        return False


def check_win(board):
    if check_diagonal(board) or check_vertical(board) or check_horizontal(board):
        return True


print("\nWelcome to TIC-TAC-TOE!\n")

build_board()
current_player_name = "Player1"
current_player_sign = "X"

while True:

    replace_num = input(f"\n{current_player_name} select a number: ")
    print("\n")
    update_board(board, replace_num, current_player_sign)
    if check_win(board):
        print(f"{current_player_name} wins!")
    change_current_player()
