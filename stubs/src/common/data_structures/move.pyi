import uuid as uuid_lib
from .profiles import Player as Player
from typing import Any

class Move:
    game_uuid: Any
    player: Any
    def __init__(self, game_uuid: uuid_lib.UUID, player: Player, move_uuid: uuid_lib.UUID = ...) -> None: ...

class MoveSkip(Move): ...

class MoveTile(Move):
    row: Any
    column: Any
    def __init__(self, game_uuid: uuid_lib.UUID, player: Player, row: int, column: int, move_uuid: uuid_lib.UUID = ...) -> None: ...

class MoveTower(MoveTile): ...
