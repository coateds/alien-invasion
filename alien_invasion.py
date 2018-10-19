import os
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initilize  pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a shipe.
    ship = Ship(ai_settings, screen)

    # Start the main loop
    while True:
        
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

