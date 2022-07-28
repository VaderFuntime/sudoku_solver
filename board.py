import pprint

SIZE = 9


class Tile:
    def __init__(self, val=None, is_const=False):
        self.val, self.is_const = val, is_const

    def __repr__(self):
        if self.val is None:
            return "_"
        # return f"*{self.val}*" if self.is_const else str(self.val)
        return str(self.val)


class Board:
    def __init__(self):
        self.mat = [[Tile() for i in range(SIZE)] for j in range(SIZE)]

    @staticmethod
    def check_args(row, col, val):
        if val not in range(1, 10):
            raise AttributeError(f"Invalid val = {val}")
        if row not in range(SIZE):
            raise AttributeError(f"Invalid row = {row}")
        if col not in range(SIZE):
            raise AttributeError(f"Invalid col = {col}")

    def init_tile(self, row, col, val):
        self.check_args(row, col, val)

        tile = self.mat[row][col]
        if tile.is_const:
            raise AttributeError("This tile was already initialized")
        tile.val, tile.is_const = val, True
        if not self.is_valid(row, col):
            raise ValueError("Value placement is causing violations")

    def set_tile(self, row, col, val) -> bool:
        self.check_args(row, col, val)

        tile = self.mat[row][col]
        if tile.is_const:
            raise AttributeError("Trying to initialize a constant tile")
        tile.val = val
        return self.is_valid(row, col)

    def is_valid(self, row, col):
        """Returns True if the value in [row, col] has no violations, False otherwise"""
        return all([self.is_valid_row(row, col),
                    self.is_valid_col(row, col),
                    self.is_valid_box(row, col)])

    def is_valid_row(self, row, col):
        """Returns True if the value in [row, col] has no ROW violations. False otherwise"""
        val = self.mat[row][col].val
        for j in range(SIZE):
            if j != col and self.mat[row][j].val == val:
                return False
        return True

    def is_valid_col(self, row, col):
        """Returns True if the value in [row, col] has no COL violations. False otherwise"""
        val = self.mat[row][col].val
        for i in range(SIZE):
            if i != row and self.mat[i][col].val == val:
                return False
        return True

    def is_valid_box(self, row, col):
        """Returns True if the value in [row, col] has no BOX violations. False otherwise"""
        val = self.mat[row][col].val
        box_row = row // 3
        box_col = col // 3
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if (i, j) != (row, col) and self.mat[i][j].val == val:
                    return False
        return True

    def reset_tile(self, row, col):
        self.mat[row][col].val = None

    def __str__(self):
        return pprint.pformat(self.mat, width=40)
