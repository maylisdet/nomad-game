from common.interfaces.i_ihm_game_calls_data import I_IHMGameCallsData

from typing import Dict, List, Tuple
import uuid as uuid_lib
from common import Move, LocalGame, Player, Message, Profile
from uuid import uuid4


class IhmGameCallsDataImpl(I_IHMGameCallsData):
    def check_move_in_local_game(self, move: Move) -> bool:
        pass

    def leave_local_game(self) -> uuid_lib.UUID:
        pass

    def get_local_game(self) -> LocalGame:

        mayo = Player("Mayo", uuid4())
        clement = Player("Clement", uuid4())

        local_game = LocalGame("SuperGame", mayo, 140)
        local_game.define_red_player(clement)
        local_game.define_white_player(mayo)
        return local_game

    def get_local_game_grid(self) -> Dict:
        pass

    def get_local_players(self) -> Tuple[Profile, Profile]:

        mayo = Profile("Mayo", "Server", 80, 111, 77, 90, uuid4())
        clement = Profile("Clement", "Server", 80, 20, 10, 0, uuid4())
        return mayo, clement

    def get_local_game_spectators(self) -> List[Player]:
        mayo = Player("Mayo", uuid4())
        return [mayo]

    def get_local_game_messages(self) -> List[Message]:
        pass

    def is_local_game_finished(self) -> bool:
        pass

    def get_local_winner(self) -> Player:
        pass

    def clear_local_game(self) -> None:
        pass
