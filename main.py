import pygame
from constants import *
from player import *
from circleshape import *

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
    draw_player = Player(x,y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        draw_player.draw(screen)
        pygame.display.flip()
        print(dt)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()