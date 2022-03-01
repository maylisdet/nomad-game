import asyncio
from asyncio.events import AbstractServer
from common import Move
from typing import Dict, List, Optional, Any
from uuid import *
from common.data_structures.message import Message

from common.utils import threaded
from config import config
from server import (
    I_CommServerCallsData,
    I_IHMServerCallsComm,
    create_server,
    IO,
    MessageTypesToClients,
    MessageTypesToServer,
    LocalGame,
    Profile,
    PublicGame,
    Move,
)


class ComController:
    """
    ComController class

    """

    def __init__(self) -> None:
        self.__impl_interface_for_ihm_server: IHMServerCallsComm_Impl = (
            IHMServerCallsComm_Impl(self)
        )
        self.__impl_comm_calls_data: Optional[I_CommServerCallsData] = None
        self.__server: Optional[AbstractServer] = None
        self.__callback: Callback = Callback(self)

    def get_interface_for_ihm_server(self) -> I_IHMServerCallsComm:
        return self.__impl_interface_for_ihm_server

    def set_interface_from_data(self, comm_calls_data: Optional[I_CommServerCallsData]):
        self.__impl_comm_calls_data = comm_calls_data

    def get_impl_comm_calls_data(self) -> I_CommServerCallsData:
        assert self.__impl_comm_calls_data is not None
        return self.__impl_comm_calls_data

    def get_server(self) -> AbstractServer:
        assert self.__server is not None
        return self.__server

    @threaded
    def init_server(self, port: Optional[int]) -> None:
        ip = config.get("connection_info")["ip"]
        if not port:
            port = config.get("connection_info")["port"]

        async def init():
            print(f"Starting the server on port {port}...")
            self.__server = await create_server(port, ip)
            self.__callback.set_callback_server()
            await self.get_server().serve_forever()

        asyncio.run(init())


class Callback:
    def __init__(self, controller: ComController) -> None:
        self.__controller = controller

    def set_callback_server(self) -> None:
        IO.on(
            MessageTypesToServer.spectator_connection, self.handle_spectator_connection
        )
        IO.on(
            MessageTypesToServer.spectator_disconnection,
            self.handle_spectator_disconnection,
        )
        IO.on(MessageTypesToServer.canceled_game, self.handle_canceled_game)
        IO.on(MessageTypesToServer.new_game, self.handle_new_game)
        IO.on(MessageTypesToServer.player_join_game, self.handle_player_join_game)
        IO.on(
            MessageTypesToServer.new_player_connection,
            self.handle_new_player_connection,
        )
        IO.on(MessageTypesToServer.get_profile, self.handle_get_profile)
        IO.on(MessageTypesToServer.game_move, self.handle_game_move)
        IO.on(MessageTypesToServer.message, self.handle_message)
        IO.on(MessageTypesToServer.update_profile, self.handle_update_profile)
        IO.on(MessageTypesToServer.user_disconnection, self.handle_user_disconnection)

    def handle_spectator_connection(self) -> None:
        pass

    def handle_spectator_disconnection(self) -> None:
        pass

    def handle_canceled_game(self) -> None:
        pass

    def handle_new_game(self, data: LocalGame, io: IO) -> None:
        public_game = self.__controller.get_impl_comm_calls_data().create_game(data)
        io.write({"id": MessageTypesToClients.create_game_success, "data": data})
        io.broadcast(
            {"id": MessageTypesToClients.new_game_available, "data": public_game}
        )

    def handle_player_join_game(self, data: dict, io: IO) -> None:
        user_id = data["user_id"]
        game_id = data["game_id"]
        local_game = self.__controller.get_impl_comm_calls_data().add_player_to_game(
            game_id, user_id
        )
        public_game = PublicGame(local_game.status, local_game.name, game_id)
        game_owner = local_game.game_creator.uuid
        red_player = local_game.red_player
        white_player = local_game.white_player

        if red_player is None or white_player is None:
            raise Exception("at leat one player is missing")

        new_player = (
            red_player if red_player and red_player.uuid != game_owner else white_player
        )
        io.write({"id": MessageTypesToClients.join_game_success, "data": local_game})
        io.write_to(
            {"id": MessageTypesToClients.opponent_found, "data": new_player},
            game_owner,
        )
        io.broadcast(
            {"id": MessageTypesToClients.update_game_status, "data": public_game}
        )

    def handle_new_player_connection(self, data: Profile, io: IO) -> None:
        io.socket_id_map[data.uuid] = io.socket_id
        player = self.__controller.get_impl_comm_calls_data().add_user(data)
        player_list = self.__controller.get_impl_comm_calls_data().get_players()
        game_list = self.__controller.get_impl_comm_calls_data().get_available_games()
        io.write(
            {
                "id": MessageTypesToClients.connection_success,
                "data": {"players": player_list, "games": game_list},
            }
        )
        io.broadcast_to_others({"id": MessageTypesToClients.new_player, "data": player})

    def handle_get_profile(self) -> None:
        pass

    def handle_game_move(self, data: Move, io: IO) -> None:
        move = data
        game_uuid = move.game_uuid

        self.__controller.get_impl_comm_calls_data().add_move(move)

        players = self.__controller.get_impl_comm_calls_data().get_game_players(
            game_uuid
        )

        spectators = self.__controller.get_impl_comm_calls_data().get_game_spectators(
            game_uuid
        )

        is_finished = self.__controller.get_impl_comm_calls_data().is_game_finished(
            game_uuid
        )

        receivers: List[UUID] = []
        for play in players:
            receivers.append(play.uuid)
        for spec in spectators:
            receivers.append(spec.uuid)

        for player in receivers:
            io.write_to(
                {
                    "id": MessageTypesToClients.handle_move,
                    "data": {"move": move, "is_finished": is_finished},
                },
                player,
            )

        # if is_finished:
        #     (
        #         player_1,
        #         player_2,
        #     ) = self.__controller.get_impl_comm_calls_data().apply_result_to_profile(
        #         game_uuid
        #     )
        #     if player_1:
        #         io.write_to(
        #             {"id": MessageTypesToClients.update_profile, "data": player_1},
        #             player_1.uuid,
        #         )
        #     if player_2:
        #         io.write_to(
        #             {"id": MessageTypesToClients.update_profile, "data": player_2},
        #             player_2.uuid,
        #         )
        #     self.__controller.get_impl_comm_calls_data().delete_game(game_uuid)
        #     io.broadcast({"id": MessageTypesToClients.delete_game, "data": game_uuid})

    def handle_message(self, data: Message, io: IO) -> None:
        self.__controller.get_impl_comm_calls_data().add_message_to_game(
            data.game_uuid, data
        )
        players = self.__controller.get_impl_comm_calls_data().get_game_players(
            data.game_uuid
        )
        spectators = self.__controller.get_impl_comm_calls_data().get_game_spectators(
            data.game_uuid
        )
        receivers: List[UUID] = []
        for player in players:
            receivers.append(player.uuid)
        for spectator in spectators:
            receivers.append(spectator.uuid)

        for receiver in receivers:
            io.write_to(
                {"id": MessageTypesToClients.new_message, "data": data}, receiver
            )

    def handle_update_profile(self) -> None:
        pass

    def handle_user_disconnection(self, data: Profile, io: IO) -> None:
        io.broadcast(
            {"id": MessageTypesToClients.player_disconnected, "data": data.uuid}
        )
        io.socket_id_map.pop(data.uuid)


class IHMServerCallsComm_Impl(I_IHMServerCallsComm):
    def __init__(self, controller: ComController) -> None:
        super().__init__()
        self.comm_controller = controller

    def quit_server(self) -> None:
        pass

    async def start_server(self, port: int) -> None:
        self.comm_controller.init_server(port)
