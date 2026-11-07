import pygame
from geometry import Rectangle


def run_visualizer(rectangle: Rectangle):
    pygame.init()

    WIDTH, HEIGHT = 900, 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Object Visualizer")

    BACKGROUND = (18, 20, 29)
    screen.fill(BACKGROUND)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
