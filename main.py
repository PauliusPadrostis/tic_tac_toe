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





print("\nWelcome to TIC-TAC-TOE!\n")

build_board()
current_player_name = "Player1"
current_player_sign = "X"

while True:


    replace_num = input(f"\n{current_player_name} select a number: ")
    print("\n")
    update_board(board, replace_num, current_player_sign)
    change_current_player()


