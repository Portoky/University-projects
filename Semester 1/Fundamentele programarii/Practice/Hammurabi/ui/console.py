from repo.repo import RepoException
from service.service import GameOver


class Console:
    def __init__(self, service):
        self.__service = service

    def get_command(self):
        acres_to_buy_sell = int(input("Acres to buy/sell (+/-)-> "))
        units_to_feed = int(input("Units to feed the population -> "))
        acres_to_plant = int(input("Acres to plant -> "))

        return acres_to_buy_sell, units_to_feed, acres_to_plant

    def run_game(self):
        for i in range(5):
            self.display_stat()
            try:
                acres_to_buy_sell, units_to_feed, acres_to_plant = self.get_command()
                self.__service.buy_sell_acres(acres_to_buy_sell)
                self.__service.feed(units_to_feed)
                self.__service.plant(acres_to_plant)
            except RepoException as re:
                print(re)
            except GameOver as ge:
                print(ge)
                break
            except ValueError:
                print("Invalid input")
            else:
                self.__service.rat_infestation()
                self.__service.new_year()

        if self.__service.win:
            print("You Won")
        else:
            print("You lost")

    def display_stat(self):
        print(self.__service.get_data())
