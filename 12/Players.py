from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    @abstractmethod
    def get_move(self, board):
        pass


class SimplePlayer(Player):
    def get_move(self, board):
        for index, place in enumerate(board[1:]):
            if place == '_':
                return index + 1
