import os
import sys

import pygame


FPS = 50
WIDTH = 800
HEIGHT = 450


def load_image(name, color_key=None):
    fullname = os.path.join('../data', name)
    if not os.path.isfile(fullname):
        print(f'Такого файла нет')
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image
