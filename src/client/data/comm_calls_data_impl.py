from __future__ import annotations

from common.interfaces.i_comm_calls_data import I_CommCallsData

from typing import List, Union
import uuid as uuid_lib
from common import LocalGame, Player, PublicGame, Move, Message, Profile
from common.utils import hard_coded_profile
from typing import TYPE_CHECKING
from common import GameStatus

if TYPE_CHECKING:
    from client.data.data_controller import DataController


class CommCallsDataImpl(I_CommCallsData):
    def __init__(self, data_controller: DataController):
        self.data_controller = data_controller

    def store_connected_user(self, players: List[Player]):
        for player in players:
            if player not in self.data_controller.connected_players:
                self.data_controller.connected_players.append(player)

    def store_games(self, games: List[PublicGame]):
        for game in games:
            if game not in self.data_controller.public_games:
                self.data_controller.public_games.append(game)

    def add_connected_user(self, player: Player):
        if player not in self.data_controller.connected_players:
            self.data_controller.connected_players.append(player)

    def store_new_game(self, public_game: PublicGame):
        if public_game not in self.data_controller.public_games:
            self.data_controller.public_games.append(public_game)

    def player_join_game(self, player: Union[Profile, None]):
        if self.data_controller.local_game is not None:
            if self.data_controller.local_game.red_player is None:
                self.data_controller.local_game.red_player = player
            elif self.data_controller.local_game.white_player is None:
                self.data_controller.local_game.white_player = player
        else:
            raise Exception("Local game is None")

    def update_public_game(self, public_games: PublicGame) -> None:
        for i, elem in enumerate(self.data_controller.public_games):
            if elem.uuid == public_games.uuid:
                self.data_controller.public_games[i] = public_games
                return None
        print("game not found")

    def remove_local_game(self) -> None:
        pass

    def store_current_game(self, local_game: LocalGame) -> None:
        self.data_controller.local_game = local_game

    def store_local_game(self, local_game: LocalGame) -> None:
        self.data_controller.local_game = local_game

    def add_spectator_in_game(self, player: Player) -> None:
        pass

    def remove_disconnect_player(self, user_id: uuid_lib.UUID) -> None:
        self.data_controller.connected_players = [
            player
            for player in self.data_controller.connected_players
            if player.uuid != user_id
        ]

    def remove_spectator(self, user_id: uuid_lib.UUID) -> None:
        pass

    def add_move_to_local_game(self, move: Move, game_finished: bool) -> None:
        if self.data_controller.local_game is None:
            return
        if move.get_index() == "":  # skip turn
            self.data_controller.local_game.moves.append(move)
        else:
            if move.get_type() == "Pown":
                self.data_controller.local_game.board[move.get_index()] = (
                    self.data_controller.local_game.get_str_player(),
                    self.data_controller.local_game.board[move.get_index()][1] + 1,
                )
                self.data_controller.local_game.tiles_remaining -= 1
                self.data_controller.local_game.moves.append(move)
            if move.get_type() == "Tower":
                self.data_controller.local_game.board[move.get_index()] = (
                    "Tower",
                    self.data_controller.local_game.board[move.get_index()][1] + 1,
                )
                self.data_controller.local_game.nb_towers = (
                    int(self.data_controller.local_game.nb_towers) - 1
                )
                self.data_controller.local_game.moves.append(move)
        if game_finished:
            self.data_controller.local_game.status = GameStatus.FINISHED

    def add_new_message(self, message: Message) -> None:
        # test if localgame is none
        if self.data_controller.local_game is not None:
            self.data_controller.local_game.add_message(message)
        else:
            raise Exception("Local game is None")

    def remove_pending_game(self, game_id: uuid_lib.UUID) -> None:
        pass

    def update_user_profile(self, profile: Profile) -> None:
        pass

    def get_profile(self) -> Profile:
        if self.data_controller.myself is not None:
            return self.data_controller.myself.get_profile()
        else:
            raise Exception("No local user found, no profile can be provided")
