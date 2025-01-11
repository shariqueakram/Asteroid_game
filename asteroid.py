import pygame
from player import *
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(x, y)
        self.radius = radius
    def draw(self, surface):
        pygame.draw.circle(surface,(255,255,255),(self.position.x,self.position.y),self.radius,width=2)
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return        
        random_angle = random.uniform(20, 50)

        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_velocity1 *= 1.2
        new_velocity2 *= 1.2

        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2

        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)