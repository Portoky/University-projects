"""

@author: radu

 
"""
from ro.ubb.tictactoe.player.player import Player


class Computer(Player):
    def __init__(self, name, board, strategy):
        super().__init__(name, board)
        self.__strategy = strategy

    @property
    def name(self):
        return self._name

    def move(self, x, y, value):
        cell = self.__strategy.move(value)
        return cell

    def __str__(self):
        return f"{self.name}, Computer"
