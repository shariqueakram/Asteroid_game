from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame

class Player(CircleShape):
    
    def __init__ (self,x,y,shootables):
        self.shoot_cooldown_timer = 0
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shootables = shootables
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self,dt):
        self.rotation += (dt * PLAYER_TURN_SPEED)

    def update(self, dt,events=None):
        keys = pygame.key.get_pressed()
        max(self.shoot_cooldown_timer - dt,0)
        
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if events:
            for event in events:
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) and self.shoot_cooldown_timer <= 0:
                    self.shoot()
                    self.shoot_cooldown_timer = max(PLAYER_SHOOT_COOLDOWN, 0.0)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        # Use the same forward vector calculation as the move method
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Scale it by PLAYER_SHOOT_SPEED
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shootables.add(new_shot)

        