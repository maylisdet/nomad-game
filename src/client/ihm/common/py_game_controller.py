from typing import Optional

import pygame
import pygame_gui

from client.ihm.common.component import Component
from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View

FPS = 60
DIVIDER = 1000.0


class PyGameController:
    def __init__(self) -> None:
        self.ui = UIRenderer()

    def show_view(self, view: View) -> None:
        self.ui.show_view(view)

    def get_current_view(self) -> Optional[View]:
        return self.ui.current_view

    def update_component(self, component: Component) -> None:
        self.ui.update_component(component)

    def get_ui_manager(self) -> pygame_gui.UIManager:
        return self.ui.get_pygame_manager()

    def get_ui_renderer(self) -> UIRenderer:
        return self.ui

    def run_main_loop(self) -> None:
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(FPS) / DIVIDER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.USEREVENT:
                    self.ui.handle_event(event)

                self.ui.get_pygame_manager().process_events(event)

                self.ui.handle_game_loop(time_delta)
