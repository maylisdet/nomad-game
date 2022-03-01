import uuid as uuid_lib
from .message import Message as Message
from .move import Move as Move
from .profiles import Player as Player, Profile as Profile
from .square import Square as Square
from typing import Any, List

class LocalGame:
    game_round: Any
    chat: Any
    squares_list: Any
    game_creator: Any
    black_player: Any
    red_player: Any
    status: Any
    nb_towers: Any
    tiles_remaining: Any
    name: Any
    def __init__(self, name: str, tiles_remaining: int, nb_towers: int, status: str, red_player: Player, black_player: Player, game_creator: Player, squares_list: List[List[Square]], game_round: int, chat: Message, game_uuid: uuid_lib.UUID = ...) -> None: ...
