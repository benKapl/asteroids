import pygame

from constants import *

def main():
    pygame.init()
    # creates screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(color="black")

    clock = pygame.time.Clock()
    dt = 0
    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000
    
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()