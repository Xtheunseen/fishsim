import pygame
import random
from fish import Fish
from game import Game

def main():
    pygame.init()
    game = Game()
    game.initialise_fishes(10)
    game.run()


if __name__ == '__main__':
    main()  