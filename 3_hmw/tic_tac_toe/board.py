from exces import OutOfBoard, AlreadyChosen


class Board:
    def __init__(self):
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.free_cells = []
        self.update_free_cells()

    def get_cell_at(self, i: int, j: int):
        if i not in range(3) or j not in range(3):
            raise OutOfBoard('Chosen out of board cell')
        return self._data[i][j]

    def set_cell_at(self, i: int, j: int, value: int):
        if i not in range(3) or j not in range(3):
            raise OutOfBoard('Chosen out of board cell')
        if (i, j) not in self.free_cells:
            raise AlreadyChosen(f'({i}, {j} cell is already chosen')

        self._data[i][j] = value
        self.update_free_cells()

    def update_free_cells(self):
        self.free_cells = []
        for i in range(3):
            for j in range(3):
                if self._data[i][j] == 0:
                    self.free_cells.append((i, j))

    def _get_horizontals(self):
        return self._data

    def _get_verticals(self):
        return [[self._data[j][i] for j in range(3)] for i in range(3)]

    def _get_diagonals(self):
        return [[self._data[i][i] for i in range(3)], [self._data[i][2 - i] for i in range(3)]]
