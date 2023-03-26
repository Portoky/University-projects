from Domain.Player import Player

class ValidatorException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

class PlayerValidator:
    def validate(self, player):
        if player.id == "" or not isinstance(player, Player):
            raise ValidatorException("Invalid ID")