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

    def get_profile(self) -> Profile:
        return Profile(
            nickname=self.nickname,
            server_name=self.server_name,
            games_won=self.games_won,
            games_lost=self.games_lost,
            games_draw=self.games_draw,
            server_port=self.server_port,
            predefined_uuid=self.uuid,
        )

    def update_user(self, profile: Profile) -> None:
        self.nickname = profile.nickname
        self.server_name = profile.server_name
        self.games_won = profile.games_won
        self.games_lost = profile.games_lost
        self.games_draw = profile.games_draw
        self.server_port = profile.server_port
        self.uuid = profile.uuid

    def __repr__(self) -> str:
        return f"Object: {self}"

    def __str__(self) -> str:
        return f"User {self.nickname} : {self}"
