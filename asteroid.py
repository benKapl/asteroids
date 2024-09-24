import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


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
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position[0], self.position[-1], new_radius)
        asteroid_a.velocity = vector_a * 1.2
        asteroid_b = Asteroid(self.position[0], self.position[-1], new_radius)
        asteroid_b.velocity = vector_b * 1.2

        
    def update(self, dt):
        self.position += self.velocity * dt