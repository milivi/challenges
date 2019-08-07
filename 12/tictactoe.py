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
        """Constructor, below worked well for us ..."""
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


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    while True:
        game = TicTacToe()
        # take turns
        for turn in VALID_POSITIONS:
            if turn % 2 == 1:
                current_player = PLAYER_X
            else:
                current_player = PLAYER_O
            game.__str__()
            move = int(input(f"What's your move player {current_player}? "))

            while not game.make_move(move, current_player):
                move = int(input(f"Invalid move player {current_player}, what's your move? "))
            if game.is_won():
                print(f"Congratulations player {current_player}, you've won!")
                game.__str__()
                break
        else:
            print("Looks like a draw...")
            game.__str__()

        if input('Play again? Enter y to continue or n to finish') == 'n':
            break
