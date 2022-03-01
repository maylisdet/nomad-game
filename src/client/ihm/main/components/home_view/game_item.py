from typing import Container
import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from common import PublicGame, GameStatus


class GameItem(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        game: PublicGame,
        pos_x: int,
        pos_y: int,
        height: int,
        width: int,
        pos: int,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.set_pos_x(pos_x)
        self.set_pos_y(pos_y)
        self.set_height(height)
        self.set_width(width)
        self.game = game
        self.pos = pos
        self.join_button = None

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            container=self.container.get_gui_element(),
            object_id=ObjectID(
                class_id="@list_panel_even" if self.pos % 2 == 0 else "@list_panel_odd"
            ),
        )

        text = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((10, 0), (150, 0)),
            html_text="Partie "
            + str(self.pos)
            + "<br>nom : "
            + self.game.name
            + "<br>status : "
            + self.game.status.value,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(
                class_id="@list_panel_even_text"
                if self.pos % 2 == 0
                else "@list_panel_odd_text"
            ),
        )

        if self.game.status != GameStatus.AVAILABLE:
            join_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((200, 25), (175, 40)),
                text="Partie en cours",
                container=self.gui_element,
                manager=self.pygame_manager,
                starting_height=1,
                object_id=ObjectID(class_id="@basic_champagne_button"),
            )
            join_button.disable()
            self.join_button = join_button
        else:
            self.join_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((200, 25), (175, 40)),
                text="Rejoindre",
                container=self.gui_element,
                manager=self.pygame_manager,
                starting_height=1,
                object_id=ObjectID(class_id="@basic_champagne_button"),
            )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.join_button:
                    self.controller.handle_join_game(self.game.uuid)
