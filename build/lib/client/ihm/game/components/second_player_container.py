import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class SecondPlayerContainer(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.class_id = "@next_player_panel"
        self.width = 460  # 350
        self.height = 110  # 100
        self.pos_x = 770
        self.pos_y = 220

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id=self.class_id),
        )

        second_player_pp = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10, 5), (40, 40)),
            manager=self.pygame_manager,
            container=self.gui_element,
            image_surface=pygame.image.load("../../ressources/images/pp1.jpg"),
        )

        second_player_name_player_name = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((75, 5), (370, 40)),
            manager=self.pygame_manager,
            container=self.gui_element,
            html_text="SxSlade",
            object_id=ObjectID("@current_player_name"),
        )

        player_stat = [
            "Parties jouées",
            "Parties gagnées",
            "Matchs Nuls",
            "Parties Perdues",
        ]
        player_score = ["400", "200", "10", "190"]

        for i in range(0, 4):
            pygame_gui.elements.UITextBox(
                relative_rect=pygame.Rect((10 + (i * 110), 45), (110, 35)),
                manager=self.pygame_manager,
                container=self.gui_element,
                html_text=player_stat[i],
                object_id=ObjectID("@current_player_data_title"),
            )
            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((10 + (i * 110), 75), (110, 35)),
                manager=self.pygame_manager,
                container=self.gui_element,
                text=player_score[i],
                object_id=ObjectID("@current_player_data"),
            )

    def modify_player_class_id(self, class_id: str) -> None:
        self.class_id = class_id
        self.render()
