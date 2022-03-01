import re

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

    def validate_input(self) -> bool:
        matches = re.search(self.validate_string, self.password_text)
        if matches is None:
            self.error_label.show()
        else:
            self.error_label.hide()
        return matches is not None

    def get_input_text(self) -> str:
        return self.password_text

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.ui_element == self.text_input:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    edit_position = event.ui_element.edit_position
                    self.password_text += event.text[len(self.password_text) :]
                    event.ui_element.set_text("*" * len(event.text))
                    event.ui_element.edit_position = edit_position + 10
