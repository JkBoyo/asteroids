import pygame

from circleshape import *
from constants import *


class Shot(CircleShape):
    containers = None
    velocity = None

    def __init__(self, x, y):
        super().__init__(x, y, radius = SHOT_RADIUS)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt