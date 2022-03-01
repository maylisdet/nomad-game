from __future__ import annotations
from common.data_structures.public_game import PublicGame

from common.interfaces.i_ihm_game_calls_data import I_IHMGameCallsData

from typing import Dict, List, Optional, Tuple, Union
from common import (
    Move,
    LocalGame,
    Player,
    Message,
    Profile,
    GameStatus,
    User,
    data_structures,
)
from uuid import *

import pickle

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.data.data_controller import DataController


class IhmGameCallsDataImpl(I_IHMGameCallsData):
    def __init__(self, data_controller: DataController) -> None:
        self.data_controller = data_controller

    def check_move_in_local_game(self, move: Move) -> bool:
        pass

    def get_profile(self) -> Profile:
        if self.data_controller.myself is not None:
            return self.data_controller.myself.get_profile()
        else:
            raise Exception("No local user found, no profile can be provided")

    def leave_local_game(self):
        self.data_controller.local_game = None

    def get_local_game(self) -> LocalGame:
        # test if the local game is already created
        if self.data_controller.local_game is not None:
            return self.data_controller.local_game
        else:
            raise ValueError("Local game not created : Is None.")

    def get_local_game_grid(self) -> Dict:
        return self.get_local_game().board

    def get_local_players(self) -> Tuple[Profile, Profile]:
        # test if players are already created
        red_player: Optional[Profile] = self.get_local_game().red_player
        white_player: Optional[Profile] = self.get_local_game().white_player
        if type(red_player) == Profile and type(white_player) == Profile:
            return red_player, white_player
        else:
            raise ValueError("Some Players are None.")

    def get_local_game_spectators(self) -> List[Player]:
        mayo = Player("Mayo", uuid4())
        return [mayo]

    def get_local_game_messages(self) -> List[Message]:
        # test if the local game is already created
        if self.data_controller.local_game is not None:
            return self.data_controller.local_game.get_chat()
        else:
            raise ValueError("Local game is None.")

    def is_local_game_finished(self) -> bool:
        return self.get_local_game().status == GameStatus.FINISHED

    def get_local_game_winner(self) -> List[Profile]:
        winners: Tuple[
            Optional[Profile], Optional[Profile], List[int]
        ] = self.get_local_game().get_winner()
        res: List[Profile] = []
        for winner in winners:
            if type(winner) == Profile:
                res.append(winner)
        return res

    def clear_local_game(self) -> None:
        self.data_controller.local_game = None
