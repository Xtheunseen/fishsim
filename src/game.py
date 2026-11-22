import pygame
import random
from fish import Fish

class Game():
    def __init__ (self):
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.fishes = []

    def initialise_fishes(self, fish_number):
        for i in range (0, fish_number):
            fish = fish = Fish(f"fish{i}", 40, random.randint(2, 10))
            self.fishes.append(fish)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(("light blue"))

            for fish in self.fishes:
                fish.move()
                fish.draw(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(30) / 1000

        pygame.quit()