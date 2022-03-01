from enum import Enum


class GameStatus(Enum):
    AVAILABLE = "available"
    WAITING_PLAYER = "waiting_player"
    FINISHED = "finished"
    # TODO put other status here
