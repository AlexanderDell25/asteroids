import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroidsgroup = pygame.sprite.Group()
asteroidfieldgroup = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroidsgroup)
AsteroidField.containers = (updatable,)

def main():
    pygame.init()
    
    clock = pygame.time.Clock() # Object of the time.Clock class
    dt = 0  # sets the change of time to 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        
        for update in updatable:
            update.update(dt) # update sprites in the updateable group

        for asteroid in asteroidsgroup:
            if player.detect_collision(asteroid):
                print("Game Over")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen) # draw sprites in the drawable group

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()