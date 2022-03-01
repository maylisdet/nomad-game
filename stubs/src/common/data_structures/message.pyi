import uuid as uuid_lib
from .profiles import Player as Player
from typing import Any

class Message:
    game_uuid: Any
    player: Any
    message: Any
    timestamp: Any
    def __init__(self, game_uuid: uuid_lib.UUID, player: Player, message: str, timestamp: int, message_uuid: uuid_lib.UUID = ...) -> None: ...
