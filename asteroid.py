import pygame
import random
from circleshape import *
from constants import *
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_asteriod_1 = self.velocity.rotate(-random_angle)
            vector_asteriod_2 = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector_asteriod_1 * 1.2
            asteroid2.velocity = vector_asteriod_2 * 1.2