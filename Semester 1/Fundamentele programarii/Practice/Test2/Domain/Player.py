class Player:
    def __init__(self, id: str, name: str, strength: int):
        self.__id = id
        self.__name = name
        self.__strength = strength

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, new_strength):
        self.__strength = new_strength

    def __str__(self):
        return f"ID: {self.id} / Name: {self.name} / Strength {self.strength}"
    def __repr__(self):
        return f"ID: {self.id} / Name: {self.name} / Strength {self.strength}"


