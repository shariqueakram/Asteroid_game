import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from astrofield import AsteroidField

def main():

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)

	pygame.init()    
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	print("Starting Asteroids!")
	print("Screen width:",SCREEN_WIDTH,"\nScreen height:",SCREEN_HEIGHT)
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y)
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0,0,0))

		for entity in updatable:
			entity.update(dt)

		for entity in drawable:
			entity.draw(screen)

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				sys.exit()

		pygame.display.flip()
		dt = clock.tick(60) / 1000	
if __name__ == "__main__":
    main()
