from Domain.validators import PlayerValidator
from Repository.player_file_repo import PlayerFileRepo
from Service.player_service import PlayerService
from UI.console import Console

if __name__ == "__main__":
    validator = PlayerValidator()
    repo = PlayerFileRepo(validator)
    service = PlayerService(repo)
    console = Console(service)
    console.start_application()


