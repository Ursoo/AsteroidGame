import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position,
                           radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            self.__create_small_asteroid(self.position.x, self.position.y, split_angle)
            self.__create_small_asteroid(self.position.x, self.position.y, -split_angle)
    
    def __create_small_asteroid(self, x, y, angle):
        velocity = self.velocity.rotate(angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(x, y, radius)
        asteroid.velocity = velocity * 1.2