import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
        pygame.Surface.fill(screen, (0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000.0


if __name__ == "__main__":
    main()
