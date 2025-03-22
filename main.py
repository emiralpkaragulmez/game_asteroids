# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		pygame.Surface.fill(screen, 'black')

#		player1.draw(screen)
		for draw in drawable:
			draw.draw(screen)



		pygame.display.flip()
		dt = (clock.tick(60) / 1000)

#		player1.update(dt)
		for update in updatable:
			update.update(dt)



if __name__ == "__main__":
	main()
