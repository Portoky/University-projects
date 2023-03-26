"""

@author: radu

 
"""
from abc import abstractmethod

from ro.ubb.tictactoe.board.cell import Cell


class Strategy:
    @abstractmethod
    def move(self, *args) -> Cell:
        """
        :param args:
        :return: the new cell or None
        """
        pass
