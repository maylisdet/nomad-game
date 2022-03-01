import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from common.data_structures import Move


class GridButton(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        pos_x: int,
        pos_y: int,
        width: int,
        height: int,
        tile_number_str: str,
        class_id: str,
        key: str,
        container: Component,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.class_id = class_id
        self.key = key
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.container = container
        self.tile_number_str = tile_number_str
        self.render()

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y),
                (self.width, self.height),
            ),
            manager=self.pygame_manager,
            text=self.tile_number_str,
            object_id=ObjectID(class_id=self.class_id),
            container=self.container.gui_element,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.gui_element:
                print(self.key, "has been pressed")
                a_move = Move(
                    self.controller.local_game.get_uuid(),
                    self.controller.local_game.get_current_player(),
                    self.key,
                    "Pauwn",
                )

                if self.key in self.controller.local_game.valid_moves_pown():
                    print("Coup possible ! ")
                    # self.controller.my_interface_to_comm.place_tile(a_move)

                else:
                    print("Coup impossible !")
                    self.controller.game_view.move_not_possible_pop_up.show()
