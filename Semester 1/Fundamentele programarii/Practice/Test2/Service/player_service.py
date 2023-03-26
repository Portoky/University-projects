import random
from Repository.player_repo import PlayerRepo

class PlayerService:
    def __init__(self, player_repo: PlayerRepo):
        self.__player_repo = player_repo

    def number_of_player(self):
        return self.__player_repo.number_of_players()

    def who_won_the_round(self, idwinner: str, idloser: str):
        self.__player_repo.remove_by_id(idloser)
        winner = self.__player_repo.find_by_id(idwinner)
        winner.strength += 1
        self.__player_repo.update(winner)

    def list_all_players_descending(self):
        result = []
        for player in self.__player_repo.find_all():
            result.append(player)
        result = sorted(result, key=lambda player: player.strength, reverse=True)
        return result

    def how_many_players_should_be(self):
        powers = 2
        while powers < self.__player_repo.number_of_players():
            powers *= 2
        if powers > self.__player_repo.number_of_players():
            powers /= 2
        return int(powers)

    def random_pairs(self, players):
        pairs = []
        for i in range(0, int(len(players) / 2)):
            while True:
                player1 = players[random.randint(0, len(players)-1)]
                if player1 not in pairs:
                    pairs.append(player1)
                    break
            while True:
                player2 = players[random.randint(0, len(players)-1)]
                if player2 not in pairs:
                    pairs.append(player2)
                    break
        return pairs



    def play_qualifying_round(self):
        players_for_tournament = self.how_many_players_should_be()
        to_eliminate = self.__player_repo.number_of_players() - players_for_tournament
        players = self.list_all_players_descending()
        players_to_qualify = players[-to_eliminate * 2:]
        players_to_qualify = self.random_pairs(players_to_qualify)

        return players_to_qualify

    def play_tournament_round(self):
        players_in_tournament = self.__player_repo.find_all()

        return self.random_pairs(players_in_tournament)









