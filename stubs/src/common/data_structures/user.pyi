import uuid as uuid_lib
from .profiles import Profile as Profile
from typing import Any

class User(Profile):
    password: Any
    firstname: Any
    lastname: Any
    birthday: Any
    def __init__(self, password: str, firstname: str, lastname: str, birthday: int, nickname: str, server_name: str, server_port: int, games_won: int = ..., games_lost: int = ..., games_draw: int = ..., predefined_uuid: uuid_lib.UUID = ...) -> None: ...
