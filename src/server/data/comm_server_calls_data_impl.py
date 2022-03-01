from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from server.data.data_server_controller import DataServerController
from typing import List, Tuple
import uuid as uuid_lib
from common import (
    LocalGame,
    PublicGame,
    Player,
    Profile,
    Move,
    Message,
    I_CommServerCallsData,
    GameStatus,
)


class CommServerCallsDataImpl(I_CommServerCallsData):
    def __init__(self, data_server_controller: DataServerController):
        self.data_server_controller = data_server_controller

    def create_game(self, local_game: LocalGame) -> PublicGame:
        self.data_server_controller.game_list.append(local_game)
        return PublicGame(local_game.status, local_game.name, local_game.uuid)

    def get_players(self) -> List:
        return self.data_server_controller.profile_list

    def get_available_games(self) -> List[PublicGame]:
        available_games_list: List[PublicGame] = []
        for game in self.data_server_controller.game_list:
            if game.status == GameStatus.AVAILABLE:
                available_games_list.append(game.convert_to_public_game())
        return available_games_list

    def add_user(self, profile: Profile) -> Player:
        new_player = Player(profile.nickname, profile.uuid)
        if new_player not in self.data_server_controller.profile_list:
            self.data_server_controller.profile_list.append(profile)
        else:
            raise Exception("Player already exist")
        return new_player

    def add_spectator_to_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> LocalGame:
        pass

    def delete_spectator_from_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> None:
        pass

    def get_game_spectators(self, game_id: uuid_lib.UUID) -> List[Player]:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if game:
            return game.spectators
        else:
            raise Exception("Game not found")

    def get_game_players(self, game_id: uuid_lib.UUID) -> List[Profile]:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if game:
            listPlayer: List[Profile] = []
            if game.white_player:
                listPlayer.append(game.white_player)
            if game.red_player:
                listPlayer.append(game.red_player)
            return listPlayer
        else:
            raise Exception("Game not found")

    def delete_game(self, game_id: uuid_lib.UUID) -> None:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if game:
            self.data_server_controller.game_list.remove(game)

    def add_player_to_game(
        self, game_id: uuid_lib.UUID, user_id: uuid_lib.UUID
    ) -> LocalGame:
        game = self.data_server_controller.get_game(game_id)
        player = self.data_server_controller.get_player(user_id)
        if game.red_player and game.white_player:
            raise Exception("game is already full")
        if game.red_player:
            game.white_player = player
        else:
            game.red_player = player
        return game

    def get_profile(self, user_id: uuid_lib.UUID) -> Profile:
        pass

    def add_move(self, move: Move) -> None:
        game_id = move.game_uuid
        local_game = self.data_server_controller.find_game_with_uuid(game_id)
        if local_game is None:
            return
        if local_game.check_move_in_local_game(move):
            if move.get_index() == "":  # skip turn
                local_game.moves.append(move)
            else:
                if move.get_type() == "Pown":
                    local_game.board[move.get_index()] = (
                        local_game.get_str_player(),
                        local_game.board[move.get_index()][1] + 1,
                    )
                    local_game.tiles_remaining -= 1
                    local_game.moves.append(move)
                if move.get_type() == "Tower":
                    local_game.board[move.get_index()] = (
                        "Tower",
                        local_game.board[move.get_index()][1] + 1,
                    )
                    local_game.nb_towers = int(local_game.nb_towers) - 1
                    local_game.moves.append(move)

            if local_game.check_if_game_is_terminate():
                local_game.status = GameStatus.FINISHED
        else:
            print("le coup est mauvais")

    def is_game_finished(self, game_id: uuid_lib.UUID) -> bool:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if game is None:
            raise Exception("Game not found")
        if game.status != GameStatus.FINISHED:
            return False
        else:
            return True

    def apply_result_to_profile(
        self, game_id: uuid_lib.UUID
    ) -> Tuple[Optional[Profile], Optional[Profile]]:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if game is None:
            raise Exception("Game not found")
        white_player: Optional[Profile] = None
        red_player: Optional[Profile] = None
        if game.status == GameStatus.FINISHED:
            white_player = game.white_player
            red_player = game.red_player
            winners: List[Profile] = []
            for winner in game.get_winner():
                if isinstance(winner, Profile):
                    winners.append(winner)

            white_player = game.white_player
            red_player = game.red_player

            """ Update the white player score """
            if white_player:
                self.data_server_controller.profile_list.remove(white_player)
                if white_player not in winners:
                    white_player.games_lost += 1
                elif len(winners) == 2:
                    white_player.games_draw += 1
                else:
                    white_player.games_won += 1
                self.data_server_controller.profile_list.append(white_player)

            """ Update the red player score """
            if red_player:
                self.data_server_controller.profile_list.remove(red_player)
                if red_player not in winners:
                    red_player.games_lost += 1
                elif len(winners) == 2:
                    red_player.games_draw += 1
                else:
                    red_player.games_won += 1
                self.data_server_controller.profile_list.append(red_player)
            return (white_player, red_player)
        else:
            raise Exception("Game not finished")

    def add_message_to_game(self, game_id: uuid_lib.UUID, message: Message) -> None:
        game = self.data_server_controller.find_game_with_uuid(game_id)
        if not game:
            raise Exception("Game not found")
        game.add_message(message)

    def update_profile(self, profile: Profile) -> None:
        pass

    def delete_user(self, user_id: uuid_lib.UUID) -> None:
        self.data_server_controller.profile_list.remove(
            self.data_server_controller.get_player(user_id)
        )
