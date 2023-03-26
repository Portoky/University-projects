
"""

@author: radu

 
"""
from ro.ubb.tictactoe.board.cell import Cell


class Board:
    def __init__(self, row: int, column: int):
        self.__row = row
        self.__column = column
        self.__cells = []

        for x in range(self.__row):
            row = []
            for y in range(self.__column):
                row.append(Cell(x, y))
            self.__cells.append(row)

    @property
    def cells(self):
        return self.__cells

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    def get_by_coord(self, x, y):
        for i in range(self.__row):
            for j in range(self.__column):
                if self.__cells[i][j].line == x and self.__cells[i][j].column == y:
                    return self.__cells[i][j]
        return None
