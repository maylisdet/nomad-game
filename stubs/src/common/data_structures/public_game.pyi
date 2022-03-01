import uuid as uuid_lib
from typing import Any

class PublicGame:
    name: Any
    status: Any
    def __init__(self, status: str, name: str, game_uuid: uuid_lib.UUID = ...) -> None: ...
