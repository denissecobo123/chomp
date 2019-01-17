import numpy as np
import pandas as pd

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self, size = (3, 4)):
        self.p1 = Player()
        self.p2 = Player()
        self.turn = random.choice(self.p1, self.p2)

    def __repr__(self):
        pass

    def coin_flip(self):
        import random
        print(random.choice['Heads', 'Tails'])


class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1

    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        for r in range(row + 1):
            self.state[r][col:] = 0


class Player:
    def __init__(self, players):
        players = []
        player1 = input("Enter your name")
        player2 = input("Enter your name too")
        self.player1 = player1
        self.player2 = player2
        players.append(player1)
        players.append(player2)
        import random
        print(random.choice(players), 'Player 1 starts the game which is')

    def __repr__(self):
        pass
