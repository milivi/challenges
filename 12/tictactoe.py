from random import randrange

from Players import SimplePlayer, HumanPlayer

DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)


class TicTacToe:

    def __init__(self):
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    def __str__(self):
        """Print the board"""
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


def play():
    print('Welcome to Tic Tac Toe!')
    while True:
        game = TicTacToe()
        ai_player = SimplePlayer()
        human_player = HumanPlayer()

        # Decide who starts
        x_turn = bool(randrange(2))
        if x_turn:
            current_player = human_player
        else:
            current_player = ai_player
        current_player.start()

        for turn in VALID_POSITIONS:
            print("Current Game Board: ")
            game.__str__()
            # Figure out whose turn it is and assign them to the current_player
            current_player = human_player if x_turn else ai_player
            x_turn = not x_turn

            move = current_player.get_move(game.board)

            while not game.make_move(move, current_player.name):
                move = current_player.invalid_move(game.board)
            if game.is_won():
                print(f"Congratulations player {current_player.name}, you've won!")
                break
        else:
            # All the valid positions had to have been played but no one won
            print("Looks like a draw...")
        print("Final Board:")
        game.__str__()
        print()
        if input('Play again? Enter y to continue or n to finish ') == 'n':
            break
