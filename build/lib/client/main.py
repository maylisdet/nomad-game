import os

from client.communication.com_controller import ComControllerClient
from client.data.data_controller import DataController
from client.ihm.common.py_game_controller import PyGameController
from client.ihm.main.ihm_main_controller import IHMMainController
from client.ihm.game.ihm_game_controller import IHMGameController


def main():
    # instantiate controllers
    pygame_controller = PyGameController()
    ihm_game_controller = IHMGameController(pygame_controller)
    ihm_main_controller = IHMMainController(pygame_controller)
    data_controller = DataController()
    com_controller = ComControllerClient()

    # link implemented interfaces to controllers
    ihm_main_controller.set_my_interface_to_ihm_game(
        ihm_game_controller.get_my_interface_from_ihm_main()
    )
    ihm_main_controller.set_my_interface_to_comm(
        com_controller.get_interface_for_ihm_main()
    )
    ihm_main_controller.set_my_interface_to_data(
        data_controller.get_my_interface_from_ihm_main()
    )

    ihm_game_controller.set_my_interface_to_comm(
        com_controller.get_interface_for_ihm_game()
    )
    ihm_game_controller.set_my_interface_to_ihm_main(
        ihm_main_controller.get_my_interface_from_ihm_game()
    )

    com_controller.set_interface_from_data(data_controller.get_my_interface_from_comm())
    com_controller.set_interface_from_ihm_main(
        ihm_main_controller.get_my_interface_from_comm()
    )
    com_controller.set_interface_from_ihm_game(
        ihm_game_controller.get_my_interface_from_comm()
    )

    # initialize network listeners ON A CHILD THREAD
    # code example
    # network_thread = Thread(target=network_manager.start_listeners)
    # network_thread.start()
    # or
    # use the @threaded annotation from common.utils before the method's definition that should be threaded

    # launch the IHM main loop in the main thread
    # /!\ windows & macos, doesn't allow to execute the pygame's main loop on a child process
    # so network callbacks should be instanced on a separate thread before this call
    pygame_controller.run_main_loop()  # blocking call, will stop on user closing the pygame's window
    os.kill(os.getpid(), 9)

    # saving things, close network thread and close connections


if __name__ == "__main__":
    main()
