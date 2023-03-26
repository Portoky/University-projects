from Repository.exception import RepoException
from Domain.validators import PlayerValidator

class PlayerRepo:
    def __init__(self, validator : PlayerValidator):
        self.__players = {}
        self.__validator = validator

    def find_all(self):
        return list(self.__players.values())

    def number_of_players(self):
        return len(self.__players)

    def find_by_id(self, player_id: str):
        if player_id not in self.__players.keys():
            return None
        return self.__players[player_id]

    def add(self, player):
        self.__validator.validate(player)
        if self.find_by_id(player.id) is not None:
            raise RepoException("Player already in repo!")
        self.__players[player.id] = player

    def remove_by_id(self, player_id: str):
        if self.find_by_id(player_id) is None:
            raise RepoException("Player is not in repo!")
        del self.__players[player_id]

    def update(self, player):
        self.__validator.validate(player)
        if self.find_by_id(player.id) is None:
            raise RepoException("Player not in repo!")
        self.__players[player.id] = player
