import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(self.containers) #type: ignore


    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                             color="white",
                            center=self.position,
                            radius=self.radius, 
                            width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt