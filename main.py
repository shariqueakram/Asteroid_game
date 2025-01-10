import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from astrofield import AsteroidField
from shot import *

def main():

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shootables = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable, drawable, shootables)

	pygame.init()    
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	print("Starting Asteroids!")
	print("Screen width:",SCREEN_WIDTH,"\nScreen height:",SCREEN_HEIGHT)
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y,shootables)
	asteroid_field = AsteroidField()

	running = True
	while running:
		dt = clock.tick(60) / 1000	
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				return

		for entity in updatable:
			if isinstance(entity, Player):
				entity.update(dt, events)
			else:
				entity.update(dt)

		screen.fill((0,0,0))

		for entity in updatable:
			entity.draw(screen)
		
		for shot in shootables:
			shot.draw(screen)
			shot.update(dt)

		for entity in drawable:
			entity.draw(screen)

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				sys.exit()

		pygame.display.flip()
	pygame.quit()
if __name__ == "__main__":
    main()
