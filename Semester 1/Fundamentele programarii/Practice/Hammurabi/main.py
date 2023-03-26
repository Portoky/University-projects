from repo.repo import CountryRepo
from service.service import CountryService
from ui.console import Console

if __name__ == "__main__":
    repo = CountryRepo()
    service = CountryService(CountryRepo())
    console = Console(service)
    console.run_game()
