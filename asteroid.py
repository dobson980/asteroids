import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # If at smallest size, just remove it
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # 1) random split angle
        random_angle = random.uniform(20, 50)

        # 2) create two new velocity vectors rotated in opposite directions
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        # 4) compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 5) create two new asteroids at current position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        # 6 & 7) set velocities, slightly faster
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

        # remove the original
        self.kill()
        return [a1, a2]