"""

@author: radu

 
"""
from ro.ubb.tictactoe.player.human import Human


class Game:
    def __init__(self, board, player1, player2):
        self.__board = board
        self.__player1 = player1
        self.__player2 = player2

        self.__last_move = None

    def play(self):
        while True:
            if self.__move(self.__player1, 1):
                break
            if self.__move(self.__player2, 2):
                break

    def __move(self, player, value):
        print(player)
        line, column = -1, -1
        self.__draw_board()
        if type(player) is Human:

            line, column = self.__read_data()
        self.__last_move = player.move(line, column, value)
        winner = self.__is_winner()
        if self.__is_over(self.__last_move) or winner:
            self.__show_game_over_status()
            return True
        return False

    def __draw_board(self):
        for x in range(self.__board.row):
            print()
            for y in range(self.__board.column):
                if self.__board.cells[x][y].value == 1:
                    print(self.__player1.name, end='')
                elif self.__board.cells[x][y].value == 2:
                    print(self.__player2.name, end='')
                else:
                    print("_", end='')
        print()

    def __read_data(self):
        while True:
            try:
                line = int(input(">Please input the line:"))
                column = int(input(">Please input the column:"))
            except ValueError:
                print("Invalid input, try again")
            else:
                if line > self.__board.row -1 or line < 0 or column > self.__board.column -1 or column < 0 or self.__board.cells[line][column].value is not None:
                    print("Invalid input, try again")
                else:
                    break
        return line, column

    def __is_winner(self):
        for x in range(self.__board.row):
            for y in range(self.__board.column):
                value = self.__board.get_by_coord(x, y).value
                if value is not None:
                    neighbor1 = self.__board.get_by_coord(x - 1, y)
                    neighbor2 = self.__board.get_by_coord(x + 1, y)
                    if neighbor1 is not None and neighbor2 is not None:
                        if neighbor1.value == value and neighbor2.value == value:
                            return True
                    neighbor1 = self.__board.get_by_coord(x, y - 1)
                    neighbor2 = self.__board.get_by_coord(x, y + 1)
                    if neighbor1 is not None and neighbor2 is not None:
                        if neighbor1.value == value and neighbor2.value == value:
                            return True
                    neighbor1 = self.__board.get_by_coord(x + 1, y + 1)
                    neighbor2 = self.__board.get_by_coord(x - 1, y - 1)
                    if neighbor1 is not None and neighbor2 is not None:
                        if neighbor1.value == value and neighbor2.value == value:
                            return True
                    neighbor1 = self.__board.get_by_coord(x + 1, y - 1)
                    neighbor2 = self.__board.get_by_coord(x - 1, y + 1)
                    if neighbor1 is not None and neighbor2 is not None:
                        if neighbor1.value == value and neighbor2.value == value:
                            return True

        return False

    def __is_over(self, last_move):
        for x in range(self.__board.row):
            for y in range(self.__board.column):
                if self.__board.cells[x][y].value is None:
                    return False
        return True

    def __show_game_over_status(self):
        if self.__last_move.value == 2:
            print("You won!")
        else:
            print("The computer won!")
