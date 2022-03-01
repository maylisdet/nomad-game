import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class ConnexionFormError(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "La connexion a échoué : le pseudo ou le mot de passe est erroné."
        self.title = "Erreur"
        self.set_pos_x(600 - 125)
        self.set_pos_y(750 // 2 - 200)
        self.set_width(250)
        self.set_height(200)

    def render(self) -> None:
        self.gui_element = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height)),
            html_message=self.text,
            manager=self.pygame_manager,
            window_title=self.title,
            visible=0,
        )
        self.gui_element.dismiss_button.set_text("OK")

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def show(self) -> None:
        self.render()
        self.gui_element.show()
