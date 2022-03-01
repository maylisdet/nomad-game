from common import LocalGame
from uuid import *
from common.data_structures.game_status import GameStatus
from common.data_structures.profiles import Profile
from server import ComController
from server.data.data_server_controller import DataServerController


def test_server_init():
    data_server_controller = DataServerController()
    assert data_server_controller.get_my_interface_from_comm_server() is not None
    assert data_server_controller.game_list == []
    assert data_server_controller.profile_list == []


# Test exception is raised when trying to get a game that does not exist
def test_server_get_game_empty_game_list():
    data_server_controller = DataServerController()
    try:
        data_server_controller.get_game(UUID("00000000-0000-0000-0000-000000000000"))
    except Exception as e:
        assert True


# Test exception is raised when trying to get a player that does not exist
def test_server_get_player_empty_profile_list():
    data_server_controller = DataServerController()
    try:
        data_server_controller.get_player(UUID("00000000-0000-0000-0000-000000000000"))
    except Exception as e:
        assert True


# Test get game returns the correct game
def test_server_get_game():
    data_server_controller = DataServerController()
    game = LocalGame(
        "test_game",
        Profile("test_player"),
        2,
        2,
        GameStatus.WAITING_PLAYER,
        None,  # Careful, we can create a game without any red player or white player
        None,
        game_round=1,
    )
    data_server_controller.game_list.append(game)
    assert data_server_controller.get_game(game.uuid) == game


# Test get player returns the correct player
def test_server_get_player():
    data_server_controller = DataServerController()
    player = Profile("test_player")
    data_server_controller.profile_list.append(player)
    player2 = Profile("test_player2")
    data_server_controller.profile_list.append(player2)
    assert data_server_controller.get_player(player.uuid) == player


# Test None is returned when trying to find a game that does not exist
def test_server_find_game_empty_game_list():
    data_server_controller = DataServerController()
    assert (
        data_server_controller.find_game_with_uuid(
            UUID("00000000-0000-0000-0000-000000000000")
        )
        is None
    )


# Test find game returns the correct game
def test_server_find_game_with_uuid():
    data_server_controller = DataServerController()
    game = LocalGame(
        "test_game",
        Profile("test_player"),
        2,
        2,
        GameStatus.WAITING_PLAYER,
        None,  # Careful, we can create a game without any red player or white player
        None,
        game_round=1,
    )
    data_server_controller.game_list.append(game)
    assert data_server_controller.find_game_with_uuid(game.uuid) == game


# Test None is returned when trying to find a player that does not exist
def test_server_find_player_empty_profile_list():
    data_server_controller = DataServerController()
    assert (
        data_server_controller.find_player_with_uuid(
            UUID("00000000-0000-0000-0000-000000000000")
        )
        is None
    )


# Test find player returns the correct player
def test_server_find_player_with_uuid():
    data_server_controller = DataServerController()
    player = Profile("test_player")
    data_server_controller.profile_list.append(player)
    player2 = Profile("test_player2")
    data_server_controller.profile_list.append(player2)
    assert data_server_controller.find_player_with_uuid(player.uuid) == player
