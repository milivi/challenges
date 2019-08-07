from Players.Player import Player


class HumanPlayer(Player):
    def __init__(self):
        self.name = 'X'

    def get_move(self, board):
        move = int(input(f"What's your move player {self.name}? "))
        return move

    def start(self):
        print(f"You start player {self.name}!")

    def invalid_move(self, board):
        print("Invalid move!")
        return self.get_move(board)
