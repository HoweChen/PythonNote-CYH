import sys
import pygame
from setting import Settings


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)
    # start game
    while True:

        # get the quit event to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # fill screen with color
        screen.fill(ai_setting.bg_color)

        # re-rendering the screen with new screen
        pygame.display.flip()

run_game()
