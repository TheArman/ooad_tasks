from player import Player
from board import Board
from exces import AlreadyChosen, OutOfBoard


class Game:
    def __init__(self, player1, player2):
        self.player1: Player = player1
        self.player1.mark = 1
        self.player2: Player = player2
        self.player2.mark = 2
        self.board = Board()
        self.to_move: Player = player1
        self.winner: Player | None = None

    def choose(self, i, j):
        try:
            self.board.set_cell_at(i, j, self.to_move.mark)
        except AlreadyChosen:
            print('the cell is already chosen')
            return
        except OutOfBoard:
            print('the cell is out of board')
            return

        if self.to_move == self.player1:
            self.to_move = self.player2
        else:
            self.to_move = self.player1

    def is_over(self):
        if not self.board.free_cells:
            return True

        for i in self.board._get_horizontals():
            if all([j == 1 for j in i]):
                self.winner = self.player1
                return True
            elif all([j == 2 for j in i]):
                self.winner = self.player2
                return True

        for i in self.board._get_verticals():
            if all([j == 1 for j in i]):
                self.winner = self.player1
                return True
            elif all([j == 2 for j in i]):
                self.winner = self.player2
                return True

        for i in self.board._get_diagonals():
            if all([j == 1 for j in i]):
                self.winner = self.player1
                return True
            elif all([j == 2 for j in i]):
                self.winner = self.player2
                return True

        return False
