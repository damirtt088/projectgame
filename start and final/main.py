import os
import sys
from final_screen import main_fin
from Constant import load_image, WIDTH, HEIGHT, FPS
import pygame

def terminate():
    main_fin()
    pygame.quit()
    sys.exit()


def start_screen(screen, clock):
    intro_text = ["Лабиринт", "",
                  "Правила игры",
                  "пока их нет",
                  "нажмите любую конпку ,чтобы перейти на финальный экран"]

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    start_screen(screen, clock)


if __name__ == '__main__':
    main()

