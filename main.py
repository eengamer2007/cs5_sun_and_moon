from turtle import speed
import pygame
from math import sin,cos,pi

WIN_WIDTH = 500
WIN_HEIGHT = 500

SUN_SPEED = 1
MOON_SPEED = 0.8

SPEED_MODIFIER = 40 # higher is lower speed

PLANET_RADIUS = 50
EARTH_RADIUS = WIN_HEIGHT * 1.5
PLANET_HEIGHT = 200
PLANET_CIRCLE_RADIUS = EARTH_RADIUS + PLANET_HEIGHT + PLANET_RADIUS

CONVERT = 10 / 2 * pi

def main():
    pygame.init()
    surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    running = 1
    time = 0.27
    stuf = 0.0
    current = 1
    day = 0
    while running:
        last = stuf
        stuf = (pygame.time.get_ticks() / 1000.0)
        delta = stuf - last
        time += (delta / SPEED_MODIFIER) * ((MOON_SPEED * current) + (SUN_SPEED * (current * -1 + 1)))
        #print(time)
        if current:
            moon_time = time
            location = (
                (sin(moon_time*CONVERT) * PLANET_CIRCLE_RADIUS + (WIN_WIDTH/2))
                ,(cos(moon_time*CONVERT) * PLANET_CIRCLE_RADIUS + (2*WIN_HEIGHT + 100))
            )
            location2 = (
                (sin((((moon_time - 0.198) * 1.4) + 0.198)*CONVERT)
                * PLANET_CIRCLE_RADIUS + (WIN_WIDTH/2)),
                (cos((((moon_time - 0.198) * 1.4) + 0.198)*CONVERT)
                * PLANET_CIRCLE_RADIUS + (2*WIN_HEIGHT + 100))
            )
            if location[0] < -(PLANET_RADIUS * 1.5):
                current = 0
                time -= 0.05
                day += 0.1
                if day >= 8*3/10:
                    day -= 8*3/10
            surface.fill((0,0,0))
            pygame.draw.circle(surface, (194,197,204), location, PLANET_RADIUS)
            pygame.draw.circle(surface, (0,0,0), location2, PLANET_RADIUS)
        else:
            sun_time = time
            location = (
                (sin(sun_time*CONVERT) * PLANET_CIRCLE_RADIUS + (WIN_WIDTH/2))
                ,(cos(sun_time*CONVERT) * PLANET_CIRCLE_RADIUS + (2*WIN_HEIGHT + 100))
            )
            if location[0] < -(PLANET_RADIUS * -1.5):
                current = 1
                time -= 0.05
            surface.fill((255,255,255))
            pygame.draw.circle(surface, (255,255,0), location, PLANET_RADIUS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(surface, (0,255,0), (WIN_WIDTH/2,2*WIN_HEIGHT + 100), EARTH_RADIUS)
        pygame.display.flip()

if __name__ == "__main__":
    main()