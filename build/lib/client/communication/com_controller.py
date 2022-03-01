from uuid import UUID
from typing import Optional
from client import (
    I_IHMMainCallsComm,
    I_IHMGameCallsComm,
    I_CommCallsIHMGame,
    I_CommCallsData,
    I_CommCallsIHMMain,
    Message,
    MessageTypesToClients,
    MessageTypesToServer,
    IO,
    Move,
    Player,
    LocalGame,
    PublicGame,
    Profile,
    create_client,
)


class ComControllerClient:
    """
    ComController class

    """

    def __init__(self):
        self.__impl_interface_for_ihm_main = IHMMainCallsComm_Impl(self)
        self.__impl_interface_for_ihm_game = IHMGameCallsComm_Impl(self)
        self.__impl_comm_calls_ihm_game = None
        self.__impl_comm_calls_ihm_main = None
        self.__impl_comm_calls_data = None
        self.__callback = Callback(self)
        self.io: Optional[IO] = None

    def get_interface_for_ihm_main(self) -> I_IHMMainCallsComm:
        return self.__impl_interface_for_ihm_main

    def get_interface_for_ihm_game(self) -> I_IHMGameCallsComm:
        return self.__impl_interface_for_ihm_game

    def set_interface_from_ihm_game(
        self, comm_calls_ihm_game: I_CommCallsIHMGame
    ) -> None:
        self.__impl_comm_calls_ihm_game = comm_calls_ihm_game

    def get_interface_from_ihm_game(self) -> I_CommCallsIHMGame:
        return self.__impl_comm_calls_ihm_game

    def set_interface_from_data(self, comm_calls_data: I_CommCallsData) -> None:
        self.__impl_comm_calls_data = comm_calls_data

    def get_interface_from_data(self) -> I_CommCallsData:
        return self.__impl_comm_calls_data

    def set_interface_from_ihm_main(
        self, comm_calls_ihm_main: I_CommCallsIHMMain
    ) -> None:
        self.__impl_comm_calls_ihm_main = comm_calls_ihm_main

    def get_interface_from_ihm_main(self) -> I_CommCallsIHMMain:
        return self.__impl_comm_calls_ihm_main

    def set_io(self, connexion: Optional[IO]) -> None:
        self.__callback.set_callback_client()
        self.io = connexion

    def get_io(self) -> IO:
        assert self.io is not None
        return self.io


class Callback:
    def __init__(self, controller: ComControllerClient) -> None:
        self.__controller = controller

    def set_callback_client(self) -> None:
        IO.on(MessageTypesToClients.new_player, self.new_user_connected)
        IO.on(MessageTypesToClients.connection_success, self.connection_success)
        IO.on(MessageTypesToClients.new_game_available, self.new_pending_game)
        IO.on(MessageTypesToClients.join_game_success, self.join_game_as_player)
        IO.on(MessageTypesToClients.update_game_status, self.update_public_game)
        IO.on(MessageTypesToClients.create_game_success, self.create_game_success)
        IO.on(MessageTypesToClients.opponent_found, self.player_join_game)
        IO.on(MessageTypesToClients.handle_move, self.play_a_move)
        IO.on(MessageTypesToClients.update_profile, self.profil_edited)
        IO.on(MessageTypesToClients.delete_game, self.stop_pending_game)

    def receive_message(self, data: dict, io: IO) -> None:
        pass

    def profil_edited(self, data: dict, io: IO) -> None:
        profile = data
        self.__controller.__impl_comm_calls_data.update_user_profile(profile)

    def new_user_connected(self, player: Player, io: IO) -> None:
        self.__controller.get_interface_from_data().add_connected_user(player)
        self.__controller.get_interface_from_ihm_main().notify_new_connected_user()

    def connection_success(self, data: dict, io: IO) -> None:
        players = data["players"]
        games = data["games"]
        self.__controller.get_interface_from_data().store_connected_user(players)
        self.__controller.get_interface_from_data().store_games(games)
        self.__controller.get_interface_from_ihm_main().launch_main()

    def user_disconnected(self, data: dict, io: IO) -> None:
        pass

    def create_game_success(self, data: LocalGame, io: IO) -> None:
        self.__controller.get_interface_from_data().store_current_game(data)
        self.__controller.get_interface_from_ihm_main().start_waiting_screen()

    def new_pending_game(self, data: PublicGame, io: IO) -> None:
        self.__controller.get_interface_from_data().store_new_game(data)
        self.__controller.get_interface_from_ihm_main().notify_new_game()

    def stop_pending_game(self, data: dict, io: IO) -> None:
        pass

    def spectator_join_game(self, data: dict, io) -> None:
        pass

    def spectator_leave_game(self, data: dict, io: IO) -> None:
        pass

    def player_join_game(self, player: Player, io: IO) -> None:
        self.__controller.get_interface_from_data().player_join_game(player)
        self.__controller.get_interface_from_ihm_main().player_join_game()

    def join_game_as_player(self, data: LocalGame, io: IO) -> None:
        self.__controller.get_interface_from_data().store_local_game(data)
        self.__controller.get_interface_from_ihm_main().join_game_as_player()

    def update_public_game(self, data: PublicGame, io: IO) -> None:
        self.__controller.get_interface_from_data().update_public_game(data)
        self.__controller.get_interface_from_ihm_main().notify_new_game()

    def player_leave_game(self, data: dict, io: IO) -> None:
        game_id = data
        self.__controller.__impl_comm_calls_data.remove_pending_game(game_id)
        self.__controller.__impl_comm_calls_ihm_main.notify_game_deleted()

    def play_a_move(self, data: dict, io: IO) -> None:
        move = data["move"]
        is_finished = data["is_finished"]
        self.__controller.__impl_comm_calls_data.add_move_to_local_game(
            move, is_finished
        )
        self.__controller.__impl_comm_calls_ihm_game.update_game()


class IHMGameCallsComm_Impl(I_IHMGameCallsComm):
    def __init__(self, controller) -> None:
        self.comm_controller = controller

    def send_message(self, message: Message) -> None:
        pass

    def place_tile(self, move: Move) -> None:
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.game_move, "data": move}
        )

    def quit_spectator_interface(self, user_id: UUID, game_id: UUID) -> None:
        pass


class IHMMainCallsComm_Impl(I_IHMMainCallsComm):
    def __init__(self, controller: ComControllerClient) -> None:
        self.comm_controller = controller

    def remove_game(self, game_id: UUID) -> None:
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.canceled_game, "data": game_id}
        )

    def get_profile_info(self, user_id: UUID) -> None:
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.get_profile, "data": user_id}
        )

    def create_game(self, local_game: LocalGame) -> None:
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.new_game, "data": local_game}
        )

    def update_profile(self, profil: Profile) -> None:
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.update_profile, "data": profil}
        )

    def spectate_game(self, user_id: UUID, game_id: UUID) -> None:
        self.comm_controller.get_io().write(
            {
                "id": MessageTypesToServer.spectator_connection,
                "data": {"user_id": user_id, "game_id": game_id},
            }
        )

    def join_game(self, user_id: UUID, game_id: UUID) -> None:
        self.comm_controller.get_io().write(
            {
                "id": MessageTypesToServer.player_join_game,
                "data": {"user_id": user_id, "game_id": game_id},
            }
        )

    async def connect_to_server(self, ip: str, port: int) -> None:
        profile = self.comm_controller.get_interface_from_data().get_profile()
        self.comm_controller.set_io(await create_client(ip, port))
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.new_player_connection, "data": profile}
        )
        await self.comm_controller.get_io().on_connection_lost

    def disconnect_server(self) -> None:
        user_id = self.comm_controller.get_interface_from_data().get_profile().uuid
        self.comm_controller.get_io().write(
            {"id": MessageTypesToServer.user_disconnection, "data": user_id}
        )
        self.comm_controller.set_io(None)
