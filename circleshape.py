import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers) #type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides(self, other):
        distance = pygame.Vector2.distance_to(self.position, other.position)
        return True if distance <= (self.radius + other.radius) else False

if __name__ == "__main__":
    c = CircleShape(x= 10, y = 12, radius = 3)
    print(c.position)