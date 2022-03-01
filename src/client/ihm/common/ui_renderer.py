import typing

import pygame
import pygame_gui

import importlib.resources as pkg_resources

from client.ihm.common.component import Component
from client.ihm.common.view import View
from config import config


class UIRenderer:
    def __init__(self):
        self.current_view: typing.Optional[View] = None

        # initialize pygame and main window
        pygame.init()
        self.window_size = self.init_window_size()
        self.background = self.init_background()

        self.trigger_view_update = False
        self.to_update: typing.List[Component] = []

        # set window title
        pygame.display.set_caption(config.get("title"))
        self.window_surface = pygame.display.set_mode(self.window_size)

        with pkg_resources.path(package="config", resource="theme.json") as theme_path:
            self.pygame_manager = pygame_gui.UIManager(self.window_size, theme_path)

    def show_view(self, view: typing.Any):  # no type cause of circular imports
        """
        Permet de passer d'une vue à une autre en faisant un reset de la scène
        """
        self.current_view = view
        self.trigger_view_update = True

    def update_component(self, component: Component):
        self.to_update.append(component)

    def handle_event(self, event):
        """
        Dispatch the event on the current view
        """
        self.current_view.handle_event(event)

    def init_window_size(self):
        monitor_width = config.get("monitor")["width"]
        monitor_height = config.get("monitor")["height"]
        return monitor_width, monitor_height

    def reset_background(self):
        """
        Clean pygame scene
        """
        self.pygame_manager.clear_and_reset()

    def init_background(self):
        """
        initialize the background
        :return the background object
        """
        background = pygame.Surface(self.window_size)
        background.fill(pygame.Color(config.get("colors")["antiqueWhite_hex"]))
        return background

    def handle_game_loop(self, time_delta):
        """
        Handle update on each tick from main loop
        called by the PyGameController
        """

        # change the view if needed
        if self.trigger_view_update:
            self.reset_background()
            self.current_view.render()
            self.trigger_view_update = False

        # update components if needed
        for component in self.to_update:
            component.render()
        self.to_update.clear()

        self.pygame_manager.update(time_delta)
        self.window_surface.blit(self.background, (0, 0))
        self.pygame_manager.draw_ui(self.window_surface)
        pygame.display.update()

    def get_pygame_manager(self) -> pygame_gui.UIManager:
        return self.pygame_manager
