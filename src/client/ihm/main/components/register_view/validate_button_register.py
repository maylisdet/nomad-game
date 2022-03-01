import pygame
import pygame_gui
import datetime

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.register_view.date_input import DateInput
from common.data_structures.user import User

from config import config


class ValidateButtonRegister(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: pygame_gui.elements.UIPanel,
        first_name: FormTextInput,
        last_name: FormTextInput,
        date: DateInput,
        pseudo: FormTextInput,
        password: FormTextInput,
        confirm_password: FormTextInput,
    ) -> None:
        super().__init__(pygame_manager)

        self.first_name = first_name
        self.last_name = last_name
        self.pseudo = pseudo
        self.password = password
        self.confirm_password = confirm_password
        self.date = date

        self.container = container
        self.pygame_manager = pygame_manager

        self.set_width(250)
        self.set_height(70)

        self.set_pos_x(475)
        self.set_pos_y(575)

        self.text = "Valider"

    def render(self) -> None:

        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.get_pos_x(), self.get_pos_y(), self.get_width(), self.get_height()
            ),
            text=self.text,
            manager=self.manager,
            container=self.container,
            starting_height=2,
            object_id=ObjectID(class_id="@big_red_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    if (
                        self.first_name.validate_input()
                        & self.last_name.validate_input()
                        & self.pseudo.validate_input()
                        & self.password.validate_input()
                        & self.confirm_password.validate_input()
                    ):

                        first_name = self.first_name.get_input_text()
                        last_name = self.last_name.get_input_text()
                        pseudo = self.pseudo.get_input_text()
                        password = self.confirm_password.get_input_text()
                        confirm_password = self.confirm_password.get_input_text()
                        day = self.date.get_day_text()
                        month = self.date.get_month_text()
                        year = self.date.get_year_text()

                        user = User(
                            firstname=first_name,
                            lastname=last_name,
                            nickname=pseudo,
                            password=password,
                            birthday=int(
                                datetime.datetime(
                                    int(year), int(month), int(day), 0, 0
                                ).timestamp()
                            ),
                            server_name="",
                            server_port=80,
                        )

                        self.controller.handle_create_account(user)
