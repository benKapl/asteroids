import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    # creates screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create groups and containers
    # updatable = pygame.sprite.Group()
    # drawable = pygame.sprite.Group()
    # Player.containers = (group_a, group_b)



    # Add Player and add it to both groups
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    # player.

    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update the player position
        player.update(dt)

        # render the screen
        pygame.display.flip()
        screen.fill("black")

        dt_milliseconds = clock.tick(60)
        dt = dt_milliseconds / 1000

        player.draw(screen)
    
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()