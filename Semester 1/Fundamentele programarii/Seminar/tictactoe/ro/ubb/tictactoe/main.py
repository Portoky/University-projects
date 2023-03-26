"""

@author: radu

 
"""
from ro.ubb.tictactoe.board.board import Board
from ro.ubb.tictactoe.game import Game
from ro.ubb.tictactoe.player.computer import Computer
from ro.ubb.tictactoe.player.human import Human
from ro.ubb.tictactoe.strategy.no_strategy import NoStrategy

if __name__ == '__main__':
    # todo: validations

    board = Board(3, 3)
    strategy = NoStrategy(board)
    player1 = Computer("X", board, strategy)
    player2 = Human("0", board)
    #player1.move(-1, -1, 2)
    game = Game(board, player1, player2)
    #
    game.play()

    print("bye")
