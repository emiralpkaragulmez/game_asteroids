import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
	    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
	    self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius < ASTEROID_MIN_RADIUS:
			return
		random_degree = random.uniform(20,50)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid_the_first = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_the_second = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_the_first.velocity = pygame.math.Vector2.rotate(self.velocity, random_degree) * 1.2
		asteroid_the_second.velocity = pygame.math.Vector2.rotate(self.velocity, -random_degree) * 1.2
