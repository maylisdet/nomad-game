import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class SectionTitle(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        text: str,
        pos_x: int,
        pos_y: int,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = text
        self.container = container
        self.set_height(50)
        self.set_width(350)
        self.set_pos_x(pos_x)
        self.set_pos_y(pos_y)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            container=self.container.get_gui_element(),
            starting_layer_height=1,
        )

        panel_title = pygame_gui.elements.UITextBox(
            # Rect((x, y),(w, h))
            relative_rect=pygame.Rect((0, 0), (self.width, self.height)),
            html_text=self.text,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@panel_title_text"),
        )

        trait_panel = pygame_gui.elements.UIPanel(
            # Rect((x, y),(w, h))
            relative_rect=pygame.Rect((0, 40), (self.width, 3)),
            manager=self.manager,
            starting_layer_height=1,
            container=self.gui_element,
            object_id=ObjectID(class_id="@title_trait"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
