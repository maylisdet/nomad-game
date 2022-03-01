import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class DisconnectButton(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "Déconnexion"
        self.set_pos_x(975)
        self.set_pos_y(35)
        self.set_width(200)
        self.set_height(50)
        self.button = None

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id="@options_panel"),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((0, 5), (20, 20)),
            image_surface=pygame.image.load("./ressources/images/exit.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 5), (150, 20)),
            text=self.text,
            # wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@options_text"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.button:
                    self.controller.handle_disconnect()
