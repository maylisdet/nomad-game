import uuid as uuid_lib


class PublicGame:
    """
    Data class for containing a game's public informations

    At init : for a random game_uuid, don't set a uuid value, or set it at 0/false

    """

    def __init__(
        self,
        status: str,  # it's supposed to be an enum, but enums don't exist in python :)
        name: str,
        game_uuid: uuid_lib.UUID = uuid_lib.uuid4(),
    ) -> None:
        self.name = name
        self.status = status

    def __repr__(self):
        return f"game {self.uuid}" f"  named: {self.name}" f"  status: {self.status}"

    def __str__(self):
        return f"game {self.uuid}" f"\nnamed: {self.name}" f"\nstatus: {self.status}"


if __name__ == "__main__":
    # u = uuid_lib.uuid4();
    # print(u)
    g = PublicGame("c'est ok le status ?@??W$4t54iu", "Ouh la la the game")
    print(g)
