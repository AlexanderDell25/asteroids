import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
       pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # turns the triangle depending on the time frame and the turn speed

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:   
            self.rotate(-dt)    # rotates counter clock wise
        if keys[pygame.K_d]:
            self.rotate(dt)     # rotates clock wise
        if keys[pygame.K_w]:
            self.move(dt)       # moves forwards
        if keys[pygame.K_s]:
            self.move(-dt)      # moves backwards

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # handles vector math while rotating
        self.position += forward * PLAYER_SPEED * dt