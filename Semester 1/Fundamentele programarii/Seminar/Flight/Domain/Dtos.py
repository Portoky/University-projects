from dataclasses import dataclass


@dataclass
class AirportActivity:
    airport_name: str
    nm_of_flights: int

@dataclass
class FlightDto:
    id: str
    start_time: int
    end_time: int

@dataclass
class Interval:
    start_time: int
    end_time: int
