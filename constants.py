import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CREAM = (205,180, 120)
GREY = (128,128, 128)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CROWN = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR,"crown.png")),(44,25))