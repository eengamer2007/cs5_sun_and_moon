import pygame
from math import sin,cos,pi

WIN_WIDTH  = 750
WIN_HEIGHT = 500

def main():
    pygame.init()
    surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    running = 1
    while running:
        surface.fill((255,255,255))
        pygame.draw.rect(surface, (0,255,0), pygame.Rect(0,WIN_HEIGHT-100,WIN_WIDTH,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == "__main__":
    main()