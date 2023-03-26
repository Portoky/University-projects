"""

@author: radu

 
"""


class Cell:
    def __init__(self, line: int, column: int, value=None):
        self.__line = line
        self.__column = column
        self.__value = value

    @property
    def line(self):
        return self.__line

    @property
    def column(self):
        return self.__column

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return f"{self.line}, {self.column} -> {self.value}"
