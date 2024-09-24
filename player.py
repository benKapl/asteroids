import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        shape = pygame.draw.polygon(surface=screen, 
                                    color="white", 
                                    points=self.triangle(),
                                    width=2)