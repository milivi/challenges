from random import randrange
from time import sleep

from Players import SimplePlayer

DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)
PLAYER_X = 'X'
PLAYER_O = 'O'


class TicTacToe:

    def __init__(self):
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    def __str__(self):
        """Print the board"""
        print('Current Game board')
        print(self.board[1:4])
        print(self.board[4:7])
        print(self.board[7:10])

    def is_won(self):
        won = False
        for a, b, c in WINNING_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '_':
                won = True
        return won

    def make_move(self, number, player):
        if number in VALID_POSITIONS and self.board[number] == '_':
            self.board[number] = player
            return True
        else:
            return False


# TODO change to 'play' function and call from a games module
if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    while True:
        game = TicTacToe()
        ai_player = SimplePlayer()

        # Decide who starts
        x_turn = bool(randrange(2))
        if x_turn:
            print("You start player X!")
        else:
            print("Computer player O starts!")
            sleep(1)

        for turn in VALID_POSITIONS:
            game.__str__()
            if x_turn:
                current_player = PLAYER_X
                move = int(input(f"What's your move player {current_player}? "))
                x_turn = False
            else:
                current_player = PLAYER_O
                print()
                print(f'Player {current_player} choosing...')
                sleep(1.5)  # Make it seem more like playing against a person
                move = ai_player.get_move(game.board)
                x_turn = True

            # TODO handle if an ai player returns a bad move
            while not game.make_move(move, current_player):
                move = int(input(f"Invalid move player {current_player}, what's your move? "))
            if game.is_won():
                print(f"Congratulations player {current_player}, you've won!")
                game.__str__()
                break
        else:
            # All the valid positions had to have been played but no one won
            print("Looks like a draw...")
            game.__str__()

        if input('Play again? Enter y to continue or n to finish') == 'n':
            break
