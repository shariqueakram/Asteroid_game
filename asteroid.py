import pygame
from player import *

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