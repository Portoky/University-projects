"""

@author: radu

 
"""
from ro.ubb.tictactoe.strategy.strategy import Strategy


class NoStrategy(Strategy):
    def __init__(self, board):
        self.__board = board

    def move(self, value):
        found = False
        x = 0
        y = 0
        for x in range(self.__board.column):
            for y in range(self.__board.row):
                if self.__board.cells[x][y].value is None:
                    self.__board.cells[x][y].value = value
                    return self.__board.cells[x][y]
        return None
