from uuid import uuid4
import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from pygame_gui.elements.ui_window import UIWindow
from config import config
from common.data_structures.profiles import Player, Profile


class DrawPopupComponent(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        # Monitor Size

        window_width = config.get("monitor")["width"]
        window_height = config.get("monitor")["height"]

        self.set_width(500)
        self.set_height(320)

        self.set_pos_x((window_width * 0.25 + 50))
        self.set_pos_y((window_height * 0.25))

        self.title = "Game Finished"

        self.hide_button = None

    def render(self) -> None:

        self.gui_element = UIWindow(
            pygame.Rect(
                (self.get_pos_x(), self.get_pos_y()),
                (self.get_width(), self.get_height()),
            ),
            manager=self.manager,
            window_display_title=self.title,
            object_id=ObjectID("@move_not_possible_pop_up_window"),
        )
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((25, 30), (420, 70)),
            manager=self.pygame_manager,
            container=self.gui_element,
            text="La partie est terminée",
            object_id=ObjectID("@message_popup_game_finished"),
        )

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((9, 100), (450, 70)),
            manager=self.pygame_manager,
            container=self.gui_element,
            text="Il y a égalité !",
            object_id=ObjectID("@message_popup_game_finished"),
        )
        self.hide_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((135, 200), (200, 60)),
            text="Quitter",
            manager=self.pygame_manager,
            starting_height=1,
            container=self.gui_element,
            object_id=ObjectID(class_id="@ihm_main_pop_up_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hide_button:
                self.controller.hide_draw_window()
                self.controller.get_my_interface_to_ihm_main().ihm_game_stoped()
