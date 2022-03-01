from abc import ABC, abstractmethod

from common import Profile


class I_CommCallsIHMMain(ABC):

    """

    Interface Communications Calls IHM Main

    """

    @abstractmethod
    def close_waiting_game(self) -> None:
        pass

    @abstractmethod
    def display_user_profile(self, profile: Profile) -> None:
        pass

    @abstractmethod
    def start_waiting_screen(self) -> None:
        pass

    @abstractmethod
    def launch_spectate_game(self) -> None:
        pass

    @abstractmethod
    def join_game_as_player(self) -> None:
        pass

    @abstractmethod
    def launch_main(self) -> None:
        pass

    @abstractmethod
    def notify_new_connected_user(self) -> None:
        pass

    @abstractmethod
    def player_join_game(self) -> None:
        pass

    @abstractmethod
    def notify_new_game(self) -> None:
        pass

    @abstractmethod
    def notify_game_deleted(self) -> None:
        pass
