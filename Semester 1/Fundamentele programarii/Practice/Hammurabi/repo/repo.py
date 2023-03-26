from dataclasses import dataclass


class RepoException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class CountryRepo:
    def __init__(self):
        self.__acres_of_land = 1000
        self.__grain_stock = 2800
        self.__population = 100
        self.__starving_people = 0
        self.__harvested_unit = 3
        self.__land_price = 20
        self.__year = 1
        self.__new_people = 0
        self.__eaten_by_rats = 20
        self.__acres_planted = 0

    @property
    def acres_planted(self):
        return self.__acres_planted

    @property
    def eaten_by_rats(self):
        return self.__eaten_by_rats

    @property
    def acres_of_land(self):
        return self.__acres_of_land

    @property
    def grain_stock(self):
        return self.__grain_stock

    @property
    def population(self):
        return self.__population

    @property
    def starving_people(self):
        return self.__starving_people

    @property
    def harvested_unit(self):
        return self.__harvested_unit

    @property
    def land_price(self):
        return self.__land_price

    @property
    def year(self):
        return self.__year

    @property
    def new_people(self):
        return self.__new_people

    @acres_of_land.setter
    def acres_of_land(self, new_value):
        if new_value + self.__acres_of_land < 0:
            raise RepoException("You dont have enough acres")
        self.__acres_of_land = new_value

    @grain_stock.setter
    def grain_stock(self, new_value):
        if self.__grain_stock + new_value < 0:
            raise RepoException("You dont have enough grain!")

    @population.setter
    def population(self, value):
        self.__population = value

    @starving_people.setter
    def starving_people(self, value):
        self.__starving_people = value

    @land_price.setter
    def land_price(self, value):
        self.__land_price = value

    @year.setter
    def year(self, value):
        self.__year = value

    @new_people.setter
    def new_people(self, value):
        self.__new_people = value

    @harvested_unit.setter
    def harvested_unit(self, value):
        self.__harvested_unit = value

    @eaten_by_rats.setter
    def eaten_by_rats(self, value):
        self.__eaten_by_rats = value

    @acres_planted.setter
    def acres_planted(self, value):
        if value > self.__acres_of_land:
            raise RepoException("You dont have this many acres")
        if value > self.__population * 10:
            raise RepoException("You dont have enough people to plant")
        self.__acres_planted = value

    def find_data(self):
        line = f"In year {self.year}, {self.starving_people} people starved\n"
        line += f"{self.new_people} came to the city\n"
        line += f"City population is {self.population}\n"
        line += f"City owns {self.acres_of_land} acres of land\n"
        line += f"Harvest was {self.harvested_unit} per acre\n"
        line += f"Rats ate {self.eaten_by_rats} units\n"
        line += f"Land price is {self.land_price} units per acre\n"
        line += f"Grain stocks are {self.grain_stock} units\n"
        return line

    def __repr__(self):
        line = f"In year {self.year}, {self.starving_people} people starved\n"
        line += f"{self.new_people} came to the city\n"
        line += f"City population is {self.population}\n"
        line += f"City owns {self.acres_of_land} acres of land\n"
        line += f"Harvest was {self.harvested_unit} per acre\n"
        line += f"Rats ate {self.eaten_by_rats} units\n"
        line += f"Land price is {self.land_price} units per acre\n"
        line += f"Grain stocks are {self.grain_stock} units\n"
        return line

