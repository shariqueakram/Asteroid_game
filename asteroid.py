import pygame
from player import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, surface):
        pygame.draw.circle(surface,(255,255,255),(self.x,self.y),self.radius,width=2)
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt        