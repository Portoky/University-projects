from Domain.Dtos import AirportActivity, FlightDto, Interval
from Domain.entity import Flight




class FlightService:
    def __init__(self, file_repo):
        self.__file_repo = file_repo

    def get_all(self):
        return self.__file_repo.find_all()

    def find_by_id(self, id: str):
        return self.__file_repo.find_by_id(id)

    def add(self, id, dep_city, dep_time, arr_city, arr_time):
        flight = Flight(id, dep_city, dep_time, arr_city, arr_time)
        self.__file_repo.add(flight)

    def remove_by_id(self, id):
        self.__file_repo.remove_by_id(id)

    def list_decreasing_activity(self):
        airport_activity_dtos = self.create_airport_dtos()
        return sorted(airport_activity_dtos, key = lambda airport : airport.nm_of_flights, reverse = True)

    def list_decreasing_empty_intervals(self):
        empty_intervals = []
        flight_dtos = self.create_flight_dtos()
        if flight_dtos[0].start_time != 0:
            empty_intervals.append(Interval(0, flight_dtos[0].start_time))
        if flight_dtos[-1].end_time != 1440: #23:59:
            empty_intervals.append(Interval(flight_dtos[-1].end_time, 1440))
        for i in range(len(flight_dtos)-1):
            if flight_dtos[i].end_time < flight_dtos[i+1].start_time:
                empty_intervals.append(Interval(flight_dtos[i].end_time, flight_dtos[i+1].start_time))

        return sorted(empty_intervals, key=lambda interval: interval.end_time - interval.start_time, reverse=True)



    def create_airport_dtos(self):
        airport_activity_dtos = []
        airports = []
        for flight in self.get_all():
            airports.append(flight.arr_city)
            airports.append(flight.dep_city)

        airports = set(airports) #now we have only one instance of each

        for airport in airports:
            counter = 0
            for flight in self.get_all():
                if flight.dep_city == airport or flight.arr_city == airport:
                    counter += 1
            airport_activity_dtos.append(AirportActivity(airport, counter))

        return airport_activity_dtos

    def create_flight_dtos(self):
        flight_dtos = []
        flights_increasing_starttime = sorted(self.get_all(), key=lambda flight: flight.dep_time)
        for flight in flights_increasing_starttime:
            dto = FlightDto(flight.id, flight.dep_time, flight.arr_time)
            flight_dtos.append(dto)

        return flight_dtos

    def most_possible_flights(self):
        flights_ending_soonest = sorted(self.get_all(), key=lambda flight: flight.arr_time)
        possible_flights = [flights_ending_soonest.pop(0)]
        for flight in flights_ending_soonest:
            #checking if it does not overlap with anything
            good = True
            for chosen_flight in possible_flights:
                if flight.dep_time > chosen_flight.dep_time or flight.arr_time < chosen_flight.arr_time:
                    good = False
                    break
            if good:
                possible_flights.append(flight)

        return possible_flights


