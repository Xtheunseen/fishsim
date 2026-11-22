import pygame
import random

class Fish():
    def __init__ (self, name, size, speed):
        self.name = name
        self.size = size
        self.speed = speed
        self.x = 640
        self.y = random.randint(20, 700)
        self.direction = 1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        if self.x >= 1000:
            self.direction = 0
        if self.x <= 100:
            self.direction = 1
        if self.direction == 1:
            self.x += self.speed
            return
        self.x -= self.speed
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


