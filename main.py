import pygame

from constants import *
from player import Player

updatable = 0

def main():
    pygame.init()
    # creates screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create groups and at them to Player.containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) #type: ignore

    # Create player
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update the updatable position
        for i in updatable:
            i.update(dt)

        # render the screen
        pygame.display.flip()
        screen.fill("black")

        dt_milliseconds = clock.tick(60)
        dt = dt_milliseconds / 1000

        # Draw the drawable
        for i in drawable:
            i.draw(screen)
    
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()