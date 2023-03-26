import random

class GameOver(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class CountryService:
    def __init__(self, country_repo):
        self.__repo = country_repo

    def rat_infestation(self):
        chance = random.randint(1, 100)
        if chance <= 20:
            minus = int(self.__repo.grain_stock * 0.2)
            self.__repo.grain_stock -= minus

    def new_year(self):
        self.__repo.year += 1

    def buy_sell_acres(self, value):
        self.random_land_price()
        if value < 0:
            #selling
            self.__repo.acres_of_land += value
            self.__repo.grain_stock += value * self.__repo.land_price
        else:
            #buying
            self.__repo.grain_stock -= value * self.__repo.land_price
            self.__repo.acres_of_land += value

    def random_land_price(self):
        new_price = random.randint(15, 25)
        self.__repo.land_price = new_price

    def feed(self, units):
        self.__repo.grain_stock -= units #its subtraction basically
        people_fed = 0
        while units >= 20:
            units -= 20
            people_fed += 1

        if people_fed > self.__repo.population:
            people_fed = self.__repo.population

        self.__repo.people_starving = self.__repo.population - people_fed

        if self.__repo.people_starving > self.__repo.population // 2:
            raise GameOver("You lost! Too many people starving")

        if self.__repo.people_starving == 0:
            self.random_new_people()

    def random_new_people(self):
        new_amount = random.randint(0, 10)
        self.__repo.new_people = new_amount
        self.__repo.population += new_amount

    def harvest(self):
        self.__repo.harvested_unit = random.randint(1, 6)
        for i in range(self.__repo.acres_planted):
            self.__repo.grain_stock += self.__repo.harvested_unit

    def plant(self, acres_to_plant):
        self.__repo.grain_stock -= acres_to_plant
        self.__repo.acres_planted = acres_to_plant


    def get_data(self):
        return self.__repo.find_data()

    def win(self):
        return self.__repo.population > 100 and self.__repo.acres_of_land > 1000



