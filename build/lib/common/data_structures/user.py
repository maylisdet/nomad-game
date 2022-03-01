from common.data_structures import Profile
import uuid as uuid_lib


class User(Profile):
    """
    Data class for player's PRIVATE profiles
    Content SHOULD NOT be sent thru the network.

    At init : for a random uuid, don't set a uuid value, or set it at 0/false
    """

    def __init__(
        self,
        password: str,
        firstname: str,
        lastname: str,
        birthday: int,
        nickname: str,
        server_name: str,
        server_port: int,
        games_won: int = 0,
        games_lost: int = 0,
        games_draw: int = 0,
        predefined_uuid: uuid_lib.UUID = uuid_lib.uuid4(),
    ) -> None:
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        super().__init__(
            nickname,
            server_name,
            games_won,
            games_lost,
            games_draw,
            server_port,
            predefined_uuid,
        )

    def __repr__(self) -> str:
        return f"Object: {self}"

    def __str__(self) -> str:
        return f"User {self.nickname} : {self}"
