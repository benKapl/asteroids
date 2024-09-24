import pygame

from constants import *

def main():
    pygame.init()
    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(color="black")
        screen = pygame.display.flip()

    
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()