from enum import Enum, auto


class MessageTypesToServer(Enum):
    spectator_connection = auto()
    spectator_disconnection = auto()
    canceled_game = auto()
    new_game = auto()
    player_join_game = auto()
    new_player_connection = auto()
    get_profile = auto()
    game_move = auto()
    message = auto()
    update_profile = auto()
    user_disconnection = auto()


class MessageTypesToClients(Enum):
    connection_success = auto()
    new_player = auto()
    create_game_success = auto()
    new_game_available = auto()
    join_game_success = auto()
    update_game_status = auto()
    opponent_found = auto()
    handle_move = auto()
    update_profile = auto()
    delete_game = auto()
    player_disconnected = auto()
    new_message = auto()
