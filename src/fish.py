import pygame

class Fish():
    def __init__ (self, name, size, speed):
        self.name = name
        self.size = size
        self.speed = speed
        self.x = 640
        self.y = 360
        self.direction = 1

    def move(self):
        if self.x >= 1280:
            self.direction = 0
        if self.x <= 0:
            self.direction = 1
        if self.direction == 1:
            self.x += self.speed
            return
        self.x -= self.speed
        
        print(self.x)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x, self.y, self.size, self.size))


