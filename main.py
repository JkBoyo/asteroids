import pygame
from constants import *
from player import *

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

    Player.containers = (updateables, drawables)

    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
        )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updateable in updateables:
            updateable.update(dt)
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()