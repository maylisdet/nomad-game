import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput


class ValidateConnexionButton(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        nickname_input: FormTextInput,
        password_input: FormTextInput,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.text = "Valider"
        self.set_pos_x(180)
        self.set_pos_y(300)
        self.set_width(250)
        self.set_height(75)

        self.nickname_input = nickname_input
        self.password_input = password_input

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.gui_element.get_abs_rect().collidepoint(event.pos):
                    if (
                        self.nickname_input.validate_input()
                        & self.password_input.validate_input()
                    ):
                        self.controller.handle_connexion(
                            self.nickname_input.get_input_text(),
                            self.password_input.get_input_text(),
                        )
                        self.controller.handle_from_connexion_form_to_infos_serv()
