from typing import Union
import uuid as uuid_lib

from common.data_structures import Profile


class Move:
    def __init__(
        self,
        game_uuid: uuid_lib.UUID,
        player: Union[Profile, None],
        index: str,
        type_move: str,
    ):
        self.game_uuid: uuid_lib.UUID = game_uuid
        self.player: Union[Profile, None] = player
        self.index: str = index
        self.type_move: str = type_move

    def get_type(self) -> str:
        return self.type_move

    def get_index(self) -> str:
        return self.index
