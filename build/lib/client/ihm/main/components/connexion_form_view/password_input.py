import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput


class PasswordInput(FormTextInput):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        pos_x,
        pos_y,
        container: Component,
        labelName: str,
        required: bool,
        validation_string: str,  # is a regex !
    ) -> None:
        super().__init__(
            pygame_manager,
            pos_x,
            pos_y,
            container,
            labelName,
            required,
            validation_string,
        )
        self.password_text = ""

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYUP:
            pass
            # TODO later : transform the input into ****
            # diff = len(self.text_input.get_text()) - len(self.password_text)
            # if diff > 0:
            #     print("diff " + str(diff))
            #     print("get text : " + self.text_input.get_text())
            #     self.password_text += self.text_input.get_text()[diff:] if len(self.password_text) > 0 else self.text_input.get_text()
            #     self.text_input.set_text("*" * len(self.password_text))
            #     print("password text : " + self.password_text)
            #     print(self.password_text)
            #     self.text_input.redraw()
            #     self.text_input.cursor
            #     self.text_input.redraw_cursor()
