from sys import exit

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


    pygame.init()
    # creates screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
 

    # Contain objects within their respective groups
    Player.containers = (updatable, drawable) #type: ignore
    Asteroid.containers = (asteroids, updatable, drawable) #type: ignore
    AsteroidField.containers = (updatable)  #type: ignore 
    Shot.containers = (shots, updatable, drawable) #type: ignore

    # Create player and asteroids
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        # Allow user to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update the updatable positions
        for i in updatable:
            i.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides(asteroid):
                exit("Game over!")

        # Check for collisions betweens shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides(asteroid):
                    asteroid.kill()
                    shot.kill()

        # Render the screen (for each frame)
        pygame.display.flip()
        screen.fill("black")

        dt_milliseconds = clock.tick(60)
        dt = dt_milliseconds / 1000

        # Draw the drawable
        for i in drawable:
            i.draw(screen)

if __name__ == "__main__":
    main()