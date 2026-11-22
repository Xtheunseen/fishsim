import pygame
import random
from fish import Fish, Carp

class Game():
    def __init__ (self):
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.fish_layer1 = []
        self.fish_layer2 = []

    def initialise_fishes(self, fish_number):
        carp_num = random.randint(0, 5)
        for i in range (0, fish_number - carp_num):
            fish = Fish(f"fish{i}", 40, random.randint(2, 10))
            self.fish_layer1.append(fish)

        for i in range (0, carp_num):
            carp = Carp(f"carp{i}", 40, random.randint(2, 7))
            self.fish_layer2.append(carp)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(("black"))

            for fish in self.fish_layer1:
                if fish.species == "fish":
                    fish.move()
                elif fish.species == "carp":
                    fish.move_horizontal()
                    fish.move_vertical()
                fish.draw(self.screen)

            for fish in self.fish_layer2:
                if fish.species == "fish":
                    fish.move()
                elif fish.species == "carp":
                    fish.move_horizontal()
                    fish.move_vertical()
                fish.draw(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(30) / 1000

        pygame.quit()