from typing import List
from common import Player
from common.data_structures.public_game import PublicGame
from src.client.data.data_controller import DataController


class IhmMainCallsDataImpl:
    def get_public_games(self) -> List[PublicGame]:
        return DataController.available_games

    def get_connected_players(self) -> List[Player]:
        return DataController.connected_players
