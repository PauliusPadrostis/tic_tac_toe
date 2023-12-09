import sys

from models.game import TicTacToe
from models.player import Player

print("\nWelcome to TIC-TAC-TOE!\n")

player1 = Player("Player1", "X")
player2 = Player("Player2", "O")

player1.initiate_player_name()
player2.initiate_player_name()
print("\n")

game = TicTacToe(player1, player2)
game.build_board()

while True:
    print("\n")
    game.update_board()
    if game.check_win():
        print(f"\n{game.current_player_name} wins!")
        break
    elif game.check_if_draw():
        print("\nIt's a draw!")
        again = input("\nPlay again? (Y/N): ")
        if again.lower() == "y" or again.lower() == "yes":
            game.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
            print("\n")
            game.build_board()
            continue
        else:
            sys.exit()
    game.change_current_player()
