"""

@author: radu

 
"""
from ro.ubb.tictactoe.player.player import Player


class Human(Player):
    def __init__(self, name, board):
        super().__init__(name, board)

    @property
    def name(self):
        return self._name

    def move(self, x: int, y: int, value):
        if self._board.cells[x][y].value is not None:
            return None
        self._board.cells[x][y].value = value
        return self._board.cells[x][y]

    def __str__(self):
        return f"{self.name}, Human"

