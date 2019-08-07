from time import sleep

from Players.Player import Player


class SimplePlayer(Player):
    def get_move(self, board):
        print()
        print(f'Player {self.name} choosing...')
        sleep(1)  # Make it seem more like playing against a person
        return super().get_move(board)

    def invalid_move(self, board):
        return super().get_move(board)
