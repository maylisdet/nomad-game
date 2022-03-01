import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class ConnexionBackButton(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "Retour"
        self.set_pos_x(20)
        self.set_pos_y(680)
        self.set_width(200)
        self.set_height(50)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            manager=self.pygame_manager,
            starting_height=1,
            object_id=ObjectID(class_id="@basic_champagne_button"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.gui_element.get_abs_rect().collidepoint(event.pos):
                    print("hiiii")
