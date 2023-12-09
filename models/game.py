from models.player import *


class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.spacer = "|-------------------|"
        self.v_line = "|"
        self.h_line = "+---+---+---+"
        self.player1 = player1
        self.player2 = player2
        self.current_player_name = player1.name
        self.current_player_sign = player1.sign

    def build_board(self):

        print(self.spacer)
        for row in self.board[::-1]:
            print(f"\t{self.h_line}")
            print(f"\t{self.v_line} {row[0]} {self.v_line} {row[1]} {self.v_line} {row[2]} {self.v_line}")
        print(f"\t{self.h_line}")
        print(self.spacer)

    def update_board(self):

        while True:
            flat_board = [item for row in self.board for item in row]
            try:
                num_choice = input(f"\n{self.current_player_name} select a number: ")
                if int(num_choice) > 9:
                    print("Number outside of allowed range. Try again!")
                    continue
                elif num_choice not in flat_board:
                    print("That spot is already taken. Try again!")
                    continue
                else:
                    break
            except ValueError:
                print("Entered value is not a number. Try again!")

        row = -1
        for x in self.board:
            col = -1
            row += 1
            for xx in x:
                col += 1
                if xx == num_choice:
                    self.board[row][col] = self.current_player_sign
                    self.build_board()
                    break

    def change_current_player(self):
        if self.current_player_name == self.player1.name:
            self.current_player_name = self.player2.name
            self.current_player_sign = self.player2.sign
        else:
            self.current_player_name = self.player1.name
            self.current_player_sign = self.player1.sign

    def check_horizontal(self):
        frh = [self.board[0][0], self.board[0][1], self.board[0][2]]
        srh = [self.board[1][0], self.board[1][1], self.board[1][2]]
        trh = [self.board[2][0], self.board[2][1], self.board[2][2]]

        if frh[0] == frh[1] == frh[2]:
            return True
        elif srh[0] == srh[1] == srh[2]:
            return True
        elif trh[0] == trh[1] == trh[2]:
            return True
        else:
            return False

    def check_vertical(self):
        fcv = [self.board[0][0], self.board[1][0], self.board[2][0]]
        scv = [self.board[0][1], self.board[1][1], self.board[2][1]]
        tcv = [self.board[0][1], self.board[1][1], self.board[2][1]]

        if fcv[0] == fcv[1] == fcv[2]:
            return True
        elif scv[0] == scv[1] == scv[2]:
            return True
        elif tcv[0] == tcv[1] == tcv[2]:
            return True
        else:
            return False

    def check_diagonal(self):
        fdia = [self.board[0][0], self.board[1][1], self.board[2][2]]
        sdia = [self.board[2][0], self.board[1][1], self.board[0][2]]

        if fdia[0] == fdia[1] == fdia[2]:
            return True
        elif sdia[0] == sdia[1] == sdia[2]:
            return True
        else:
            return False

    def check_win(self):
        if self.check_diagonal() or self.check_vertical() or self.check_horizontal():
            return True

    def check_if_draw(self):
        counter = 0
        for row in self.board:
            for item in row:
                if item not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    counter += 1
                else:
                    continue
        if counter != 9:
            return False
        else:
            return True
