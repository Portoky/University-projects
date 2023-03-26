from Domain.validators import ValidatorException
from Repository.exception import RepoException
from Service.player_service import PlayerService

class Console:
    def __init__(self, player_service: PlayerService):
        self.__player_service = player_service
        self.__commands = {"start": self.start_tournament, "list": self.list}
        self.__tournament_over = False

    def start_application(self):
        print("Write -start- to start the tournament; -list- to list the players; -exit- to exit the application")
        while not self.__tournament_over:
            command, arg = self.read_command()
            if len(arg) == 0:
                if command == "exit":
                    self.__tournament_over = True
                else:
                    try:
                        self.__commands[command]()
                    except KeyError:
                        print("Option not implemented yet!")
                    except RepoException as re:
                        print(re)
                    except ValidatorException as ve:
                        print(ve)
            else:
                print("Invalid command")

    def read_command(self):
        line = input(">")
        blank = line.find(" ")
        if blank == -1:
            return line, []
        command = line[:blank]
        args = line[blank+1:]
        args = args.split()
        args = [arg.strip() for arg in args]
        return command, args

    def list(self):
        players = self.__player_service.list_all_players_descending()
        for player in players:
            print(player)

    def start_tournament(self):
        if self.__player_service.how_many_players_should_be() != self.__player_service.number_of_player():
            self.qualification_round()
        print("!!Tournament!!")
        while self.__player_service.number_of_player() > 1:
            self.tournament_round()
        print("The tournament is over!")
        self.__tournament_over = True

    def qualification_round(self):
        print("Qualification:")
        players_to_qualify = self.__player_service.play_qualifying_round()
        players_to_remain = int(len(players_to_qualify) / 2)
        for i in range(0, players_to_remain):
            while True:
                print(f"{players_to_qualify[i]} VS {players_to_qualify[i+1]}")
                opt = input("Decide which player should win 1 / 2: ")
                if opt == "1":
                    self.__player_service.who_won_the_round(players_to_qualify[i].id, players_to_qualify[i+1].id)
                    del players_to_qualify[i + 1]
                    break
                elif opt == "2":
                    self.__player_service.who_won_the_round(players_to_qualify[i+1].id, players_to_qualify[i].id)
                    del players_to_qualify[i]
                    break
                else:
                    print("Invalid input, try again")

    def tournament_round(self):
        print(f"The last {self.__player_service.number_of_player()}!")
        players = self.__player_service.play_tournament_round()
        players_to_remain = int(len(players) / 2)
        for i in range(0, players_to_remain):
            while True:
                print(f"{players[i]} VS {players[i + 1]}")
                opt = input("Decide which player should win 1 / 2: ")
                if opt == "1":
                    self.__player_service.who_won_the_round(players[i].id, players[i+1].id)
                    del players[i+1]
                    break
                if opt == "2":
                    self.__player_service.who_won_the_round(players[i+1].id, players[i].id)
                    del players[i]
                    break
                else:
                    print("Invalid input, try again")








