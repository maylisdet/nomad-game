import pygame
import pygame_gui
import re

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class FormTextInput(Component):
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
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = labelName
        self.container = container
        self.set_pos_x(pos_x)
        self.set_pos_y(pos_y)
        self.set_width(250)
        self.set_height(100)
        self.required = required
        self.validate_string = validation_string
        self.text_input: pygame_gui.elements.UITextEntryLine = None

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            container=self.container.get_gui_element(),
            starting_layer_height=1,
        )

        self.label = pygame_gui.elements.UITextBox(
            html_text=self.text
            + ("<font color='#EE6055'>*</font>" if self.required else ""),
            relative_rect=pygame.Rect((0, 0), (self.width, self.height)),
            manager=self.pygame_manager,
            wrap_to_height=True,
            container=self.gui_element,
            object_id=ObjectID(class_id="@form_label"),
        )

        self.text_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((5, 35), (self.width, self.height)),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        self.error_label = pygame_gui.elements.UITextBox(
            html_text="La valeur saisie est erronée",
            relative_rect=pygame.Rect((0, 60), (self.width, self.height)),
            manager=self.pygame_manager,
            wrap_to_height=True,
            container=self.gui_element,
            visible=0,
            object_id=ObjectID(class_id="@form_error"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def validate_input(self) -> bool:
        matches = re.search(self.validate_string, self.get_input_text())
        if matches is None:
            self.error_label.show()
            print("Erreur ici !")
        else:
            self.error_label.hide()
        return matches is not None

    def get_input_text(self) -> str:
        return self.text_input.get_text()
