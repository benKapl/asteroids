import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    # creates screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt_milliseconds = clock.tick(60)
        dt = dt_milliseconds / 1000

        # Add Player and render it
        player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
        player.draw(screen)
    
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()