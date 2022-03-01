import uuid as uuid_lib

from common.data_structures.profiles import Player


class Message:
    """
    Data class for containing text messages

    At init: for a random message_uuid, don't set a uuid value, or set it at 0/false
    """

    def __init__(
        self,
        game_uuid: uuid_lib.UUID,
        player: Player,
        message: str,
        timestamp: int,
        message_uuid: uuid_lib.UUID = uuid_lib.uuid4(),
    ):
        self.game_uuid = game_uuid
        self.player = player
        self.message = message
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"message {self.uuid}"
            f"player: {self.player.nickname}"
            f"payload : {self.message}"
        )

    def __str__(self):
        return (
            f"message {self.uuid}\n"
            f"player: {self.player.uuid}\n"
            f"payload : {self.message}"
        )
