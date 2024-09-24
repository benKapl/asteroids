import pygame

from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, 
                       PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN)
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.add(self.containers) #type: ignore
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius #type: ignore
        b = self.position - forward * self.radius - right #type: ignore
        c = self.position - forward * self.radius + right #type: ignore
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, 
                                    color="white", 
                                    points=self.triangle(),
                                    width=2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if not self.shoot_cooldown > 0:
                self.shoot()
        
        self.shoot_cooldown -= dt


    
