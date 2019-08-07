from abc import ABCMeta, abstractmethod
from time import sleep


class Player(metaclass=ABCMeta):
    def __init__(self):
        self.name = 'O'

    @abstractmethod
    def get_move(self, board):
        for index, place in enumerate(board[1:]):
            if place == '_':
                return index + 1

    def start(self):
        print(f"Computer player {self.name} starts!")
        sleep(1)

    @abstractmethod
    def invalid_move(self, board):
        pass


class SimplePlayer(Player):
    def get_move(self, board):
        print()
        print(f'Player {self.name} choosing...')
        sleep(1)  # Make it seem more like playing against a person
        return super().get_move(board)

    def invalid_move(self, board):
        return super().get_move(board)


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
