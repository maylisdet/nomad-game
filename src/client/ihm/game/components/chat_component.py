import pygame
import pygame_gui
import time
from common.data_structures import *

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class ChatComponent(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.width = 485
        self.height = 320
        self.pos_x = 690
        self.pos_y = 350
        self.send_message_button: pygame_gui.elements.UIButton
        self.chat_input: pygame_gui.elements.UITextEntryLine
        self.messages_container: pygame_gui.elements.UITextBox = None
        self.html_messages_content: str = ""

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id="@chat_panel"),
        )

        self.messages_container = pygame_gui.elements.UITextBox(
            html_text=self.html_messages_content,
            relative_rect=pygame.Rect((3, 3), (465, 275)),
            container=self.gui_element,
            manager=self.pygame_manager,
            object_id=ObjectID(class_id="@chat_msg_container"),
        )

        self.chat_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((10, 280), (370, 10)),
            manager=self.pygame_manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@chat_input"),
        )

        self.send_message_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((382, 280), (95, 24)),
            text="Envoyer",
            manager=self.pygame_manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@send_message_button"),
        )

    def set_html_messages_content(self, html_messages):
        self.html_messages_content = html_messages

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.send_message_button:
                new_msg = Message(
                    self.controller.local_game.uuid,
                    self.controller.get_my_interface_to_data().get_profile(),
                    self.chat_input.get_text(),
                    int(time.time()),
                )
                self.chat_input.set_text("")
                self.controller.get_my_interface_to_comm().send_message(new_msg)
