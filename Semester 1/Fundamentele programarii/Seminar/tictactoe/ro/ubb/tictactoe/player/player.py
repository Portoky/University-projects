"""

@author: radu

 
"""
from abc import abstractmethod

from ro.ubb.tictactoe.board.cell import Cell


class Player:
    def __init__(self, name, board):
        self._name = name
        self._board = board

    @abstractmethod
    def move(self, *args) -> Cell:
        """
        :param args:
        :return: the new cell or None
        """
        pass
