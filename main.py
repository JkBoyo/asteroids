import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    updateables = pygame.sprite.Group()

    drawables = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)

    Asteroid.containers = (asteroids, updateables, drawables)

    Shot.containers = (shots, updateables, drawables)

    AsteroidField.containers = (updateables,)

    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
        )
    
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updateable in updateables:
            updateable.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisions(asteroid):
                    asteroid.split()
                    shot.kill()


        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()