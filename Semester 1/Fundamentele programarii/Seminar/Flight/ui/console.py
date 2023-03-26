from repo.mem_repo import RepoException


class ValidatorException:
    pass


class Console:
    def __init__(self, service):
        self.__service = service
        self.__command = {"1":self.add, "2":self.remove_by_id, "3": self.list_decreasing_order,
                          "4": self.list_decreasing_time_intervals, "5": self.list_possible_flights}

    def print_options(self):
        print("1. Add a new flight")
        print("2. Remove flight")
        print("3. List decreasing activity")
        print("4. List decreasing empty intervals")
        print("5. List flights that can proceed as planned")
        print("Exit - exit the application")

    def start(self):
        while True:
            self.print_options()
            cmd = input(">Type in your command:")
            if cmd == "exit":
                break
            try:
                self.__command[cmd]()
            except RepoException as re:
                print(re)
            except ValidatorException as ve:
                print(ve)
            except KeyError:
                print("Option not implemented")

    def add(self):
        id  = input("ID: ")
        dep_city = input('Departure City: ')
        dep_time = int(input("Departure time (in minutes): "))
        arr_city = input("Arrival City: ")
        arr_time = int(input("Arrival time (in minutes): "))
        self.__service.add(id, dep_city, dep_time, arr_city, arr_time)

    def remove_by_id(self):
        id = input("ID:")
        self.__service.remove_by_id(id)

    def list_decreasing_order(self):
        for airport in self.__service.list_decreasing_activity():
            print(airport.airport_name)

    def list_decreasing_time_intervals(self):
        for interval in self.__service.list_decreasing_empty_intervals():
            start_hour = interval.start_time // 60
            start_min = interval.start_time % 60
            end_hour = interval.end_time // 60
            end_min = interval.end_time % 60
            print(f"{start_hour}:{start_min} - {end_hour}:{end_min}")

    def list_possible_flights(self):
        for flight in self.__service.most_possible_flights():
            print(flight)
