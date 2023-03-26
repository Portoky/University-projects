from Domain.Player import Player
from Repository.exception import RepoException
from Repository.player_repo import PlayerRepo

class PlayerFileRepo(PlayerRepo):
    def __init__(self, validator, file_name="players.txt"):
        super().__init__(validator)
        self.__file_name = file_name

        self.load_file()


    def load_file(self):
        try:
            fin = open(self.__file_name, "rt")
            lines = fin.readlines()
            fin.close()

        except FileNotFoundError:
            raise RepoException("FileNotFound")
        except IOError:
            pass

        for line in lines:
            elements = line.split(",")
            elements = [element.strip() for element in elements]
            player = Player(elements[0], elements[1], int(elements[2]))
            super().add(player)


    def save_file(self):
        try:
            fout = open(self.__file_name, "wt")

        except FileNotFoundError:
            raise RepoException("FileNotFound")
        except IOError:
            pass

        for player in self.find_all():
            fout.write(f"{player.id},{player.name},{player.strength}\n")

        fout.close()

    def add(self, player):
        super().add(player)
        self.save_file()

    def remove_by_id(self, player_id: str):
        super().remove_by_id(player_id)
        self.save_file()

    def update(self, player):
        super().update(player)
        self.save_file()
