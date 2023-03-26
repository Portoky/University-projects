from Domain.entity import FlightValidator
from repo.flie_repo import FileRepo
from service.service import FlightService
from ui.console import Console

if __name__ == '__main__':
    repo = FileRepo("flights.txt", FlightValidator())
    service = FlightService(repo)
    console = Console(service)
    console.start()