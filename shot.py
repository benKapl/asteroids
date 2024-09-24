import pygame

from circleshape import CircleShape

from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position[0], position[-1], radius=SHOT_RADIUS)
        self.add(self.containers) #type: ignore

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                             color="white",
                            center=self.position,
                            radius=self.radius, 
                            width=2)

    def update(self, dt):
        self.position += self.velocity * dt




        
