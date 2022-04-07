import pygame
from math import sin,cos,pi

def main():
    pygame.init()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == "__main__":
    main()