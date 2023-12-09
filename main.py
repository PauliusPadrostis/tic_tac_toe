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
        print("It's a draw!")
        break
    game.change_current_player()
