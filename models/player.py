class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def initiate_player_name(self):
        self.name = input(f"{self.name} enter your name: ")