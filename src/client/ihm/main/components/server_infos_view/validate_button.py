import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput


class ValidateButton(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        ip_address_input: FormTextInput,
        port_input: FormTextInput,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.text = "Valider"
        self.set_pos_x(180)
        self.set_pos_y(300)
        self.set_width(250)
        self.set_height(75)

        self.ip_address_input = ip_address_input
        self.port_input = port_input

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            container=self.container.get_gui_element(),
            manager=self.pygame_manager,
            starting_height=1,
            object_id=ObjectID(class_id="@big_red_button"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    if (
                        self.ip_address_input.validate_input()
                        & self.port_input.validate_input()
                    ):
                        ip_address = self.ip_address_input.get_input_text()
                        port = self.port_input.get_input_text()

                        self.controller.handle_server_connection(ip_address, port)
