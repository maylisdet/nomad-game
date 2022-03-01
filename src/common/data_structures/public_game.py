from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common import GameStatus
import uuid as uuid_lib


class PublicGame:
    """
    Data class for containing a game's public informations

    At init : for a random game_uuid, don't set a uuid value, or set it at 0/false

    """

    def __init__(
        self,
        status: GameStatus,  # it's supposed to be an enum, but enums don't exist in python :) # ballec :)
        # XD l'embiance est délétère ici
        name: str,
        game_uuid: uuid_lib.UUID = uuid_lib.uuid4(),
    ) -> None:
        self.name = name
        self.status = status
        self.uuid = game_uuid

    def __repr__(self):
        return f"game {self.uuid}" f"  named: {self.name}" f"  status: {self.status}"

    def __str__(self):
        return f"game {self.uuid}" f"\nnamed: {self.name}" f"\nstatus: {self.status}"
