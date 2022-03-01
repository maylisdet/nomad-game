import pygame
import pygame_gui
import re

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class DateInput(Component):
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

        self.day_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((5, 35), (self.width // 5, self.height)),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        self.label_slash_one = pygame_gui.elements.UITextBox(
            html_text="/",
            relative_rect=pygame.Rect((60, 30), (30, self.height)),
            manager=self.pygame_manager,
            wrap_to_height=True,
            container=self.gui_element,
            object_id=ObjectID(class_id="@form_label"),
        )

        self.month_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((80, 35), (self.width // 5, self.height)),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        self.label_slash_two = pygame_gui.elements.UITextBox(
            html_text="/",
            relative_rect=pygame.Rect((135, 30), (30, self.height)),
            manager=self.pygame_manager,
            wrap_to_height=True,
            container=self.gui_element,
            object_id=ObjectID(class_id="@form_label"),
        )

        self.year_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((155, 35), (self.width // 5, self.height)),
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
        matches_day = re.search(self.validate_string, self.get_day_text())

        matches_month = re.search(self.validate_string, self.get_month_text())

        matches_year = re.search(self.validate_string, self.get_year_text())

        if matches_day or matches_month or matches_year is None:
            self.error_label.show()
        else:
            self.error_label.hide()
        return (matches_day and matches_month and matches_year) is not None

    def get_day_text(self) -> str:
        return self.day_input.get_text()

    def get_month_text(self) -> str:
        return self.month_input.get_text()

    def get_year_text(self) -> str:
        return self.year_input.get_text()
