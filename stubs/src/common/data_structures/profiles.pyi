import uuid as uuid_lib
from typing import Any

class Profile:
    nickname: Any
    server_name: Any
    games_won: Any
    games_lost: Any
    games_draw: Any
    server_port: Any
    def __init__(self, nickname: str, server_name: str, server_port: int, games_won: int = ..., games_lost: int = ..., games_draw: int = ..., predefined_uuid: uuid_lib.UUID = ...) -> None: ...

class Player:
    nickname: Any
    uuid: Any
    def __init__(self, nickname: str, uuid: uuid_lib.UUID) -> None: ...
