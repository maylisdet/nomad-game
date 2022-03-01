import uuid as uuid_lib


class Profile:
    """
    Data class for player's publicly visible profiles
    Content can be sent to the network.

    At init : for a random uuid, don't set a uuid value, or set it at 0/false

    """

    def __init__(
        self,
        nickname: str,
        server_name: str,
        server_port: int,
        games_won: int = 0,
        games_lost: int = 0,
        games_draw: int = 0,
        predefined_uuid: uuid_lib.UUID = uuid_lib.uuid4(),
    ):
        self.uuid: uuid_lib.UUID = predefined_uuid
        self.nickname: str = nickname
        self.server_name: str = server_name
        self.games_won: int = games_won
        self.games_lost: int = games_lost
        self.games_draw: int = games_draw
        self.server_port: int = server_port

    def __repr__(self):
        return f"Nickname: {self.nickname}"

    def __str__(self):
        return f"Nickname: {self.nickname}"

    def __eq__(self, profile):
        return self.uuid == profile.uuid


class Player:
    """
    READ ME BEFORE USAGE PLEASE

    This data class is made for user identification, and will accompany a user-associated action sent thru the network,
    such as messages or nomad-moves.

    It's been designed and validated so I coded it.
    But honestly, please follow good practices and common sense, and don't use it.

    If you want to identify a user, just send their UUID.
    Else, if you want people to be able to change their nickname during the game and break our code,
    please use this class ;)

    """

    def __init__(self, nickname: str, uuid: uuid_lib.UUID):
        self.nickname: str = nickname
        self.uuid: uuid_lib.UUID = uuid

    def __str__(self):
        return f"Nickname: {self.nickname}"

    def __repr__(self):
        return f"Nickname: {self.nickname}"
