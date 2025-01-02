# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
	pygame.init()    
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print("Screen width:",SCREEN_WIDTH,"\nScreen height:",SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
