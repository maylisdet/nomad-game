import pygame
import sys
from typing import Tuple

from config import config

from server import ComController
from server.data.data_server_controller import DataServerController


def main():
    # Logic

    data_server_controller = DataServerController()
    com_server_controller = ComController()
    com_server_controller.set_interface_from_data(
        data_server_controller.get_my_interface_from_comm_server()
    )

    # IHM

    pygame.init()

    clock = pygame.time.Clock()

    # it will display on screen
    screen = pygame.display.set_mode([600, 500])

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = str(config.get("connection_info")["port"])

    input_color = pygame.Color("gray")
    text_color = pygame.Color("black")
    started_color = pygame.Color("green")
    stopped_color = pygame.Color("gray")
    background_color = pygame.Color("black")

    started = False
    do_toggle = False
    do_quit = False

    # it will set background color of screen
    screen.fill(background_color)

    # Create "port:"
    port_text = base_font.render("port:", True, text_color)

    # Text rectangle
    port_input = pygame.Rect(200, 200, 140, 50)

    # render at position stated in arguments
    screen.blit(port_text, (port_input.x - 50, port_input.y + 5))

    # Create start/stop button
    start_stop_button = pygame.Rect(200, 400, 140, 50)

    while True:
        # handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                do_quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_stop_button.collidepoint(event.pos):
                    do_toggle = True

            elif event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # Get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string formation
                else:
                    if len(user_text) < 6:
                        char = event.unicode
                        if char.isdigit():
                            user_text += event.unicode
                        elif char == " ":
                            do_toggle = True
                        elif char == "q":
                            do_quit = True

        # Handle quit
        if do_quit:
            # TODO
            # com.server.stop()
            pygame.quit()
            sys.exit()

        # Handle start / stop
        if do_toggle:
            do_toggle = False

            if not started:
                port_number = None

                try:
                    port_number = int(user_text)
                except ValueError:
                    # We should print an error here.
                    print(
                        "Invalid value in the field, using the port from the config.yaml..."
                    )
                    pass

                if not port_number:
                    port_number = config.get("connection_info")["port"]

                started = True
                com_server_controller.init_server(port_number)

            else:
                started = False
                # TODO
                # com.server.stop()

        # Update start/stop button
        button_color = started_color if started else stopped_color
        button_text = "Stop" if started else "Start"
        pygame.draw.rect(screen, button_color, start_stop_button)
        # Update start/stop text
        button_textbox = base_font.render(button_text, True, text_color)
        screen.blit(button_textbox, middle(start_stop_button, button_textbox))

        # Redraw rectangle behind port text
        pygame.draw.rect(screen, input_color, port_input)
        # Update port text
        port_textbox = base_font.render(user_text, True, text_color)
        screen.blit(port_textbox, middle(port_input, port_textbox))

        # display.flip() will update only a portion of the
        # screen to update, not full area
        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def middle(box1: pygame.Rect, box2: pygame.Surface) -> Tuple[int, int]:
    middle_x1 = box1.x + box1.w / 2
    middle_y1 = box1.y + box1.h / 2
    return int(middle_x1 - box2.get_width() / 2), int(middle_y1 - box2.get_height() / 2)


if __name__ == "__main__":
    main()
