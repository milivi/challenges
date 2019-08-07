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
