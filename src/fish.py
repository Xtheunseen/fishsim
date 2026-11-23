import pygame
import random

class Fish():
    def __init__ (self, name, size, speed):
        #name, size, speed set in constructor
        self.name = name
        self.size = size
        self.speed = speed

        #starting x position and width
        self.x = 640
        self.width = self.size

        #starting y position and height
        self.y = random.randint(20, 700)
        self.height = self.size / 3

        #starting direction
        self.direction = 1

        #colour - aimed at silvery 
        self.color = (random.randint(190, 210),
                     random.randint(190, 210),
                     random.randint(190, 230))
        
        #species is fish (used for different movement behaviours)
        self.species = "fish"

        #hitbox using x, y, width and height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        #store the current cells in the grid for optimised collision handling
        self.cells = set()

    def move(self):
        #swap direction at x = 100 and x = 1000
        if self.x >= 1000:
            self.direction = 0
        if self.x <= 100:
            self.direction = 1
        
        #add/subtract speed to/from x depending on direction
        #update hitbox 
        if self.direction == 1:
            self.x += self.speed
            self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
            return
        self.x -= self.speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        
    
    def draw(self, screen):
        #draw a rectangle using the hitbox and the colour
        pygame.draw.rect(screen, self.color, self.hitbox)

    def collided(self, other):
        print ("woah... a super collide!")


class Carp(Fish):
    #inherits fish class
    def __init__(self, name, size, speed):
        #initialise variables using super class
        super().__init__(name, size, speed)

        #size is in the range 40-100 for small-large carp
        self.size = size + random.randint(40,100)
        #change width and height from initialisation
        self.width = self.size
        self.height = self.size/2.5

        #change colour to brown-gold range 
        self.color = (random.randint(80, 150),
                     random.randint(60, 130),
                      random.randint(40, 120))

        #vertical direction for extra movement
        self.direction_vert = 0

        #species is carp so that vertical behaviour is included
        self.species = "carp"

        #create new hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.height)


    def move_vertical(self):
        #change vertical direction if at height 200 or 600
        if self.y >= 600:
            self.direction_vert = 0
        if self.y <= 200:
            self.direction_vert = 1

        #move vertically slower than horizontally
        if self.direction_vert == 1:
            self.y += self.speed / 2
            self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
            return
        self.y -= self.speed / 2
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.height)


    def move_horizontal(self):
        #move horizontal calls super move function, just separated for logic
        self.move()

    def collided(self, other_fish):

        #swap directions horizontally
        if self.x > other_fish.x:
            self.direction = 1  # move right
            other_fish.direction = 0  # move left
        else:
            self.direction = 0  # move left
            other_fish.direction = 1  # move right

        #swap directions vertically
        if self.y > other_fish.y:
            self.direction_vert = 1
            other_fish.direction_vert = 0
        else:
            self.direction_vert = 0
            other_fish.direction_vert = 1

        #push away from each other so dont immediately recollide
        if self.x > other_fish.x:
            self.x += 5
            other_fish.x -= 5
        else:
            self.x -= 5
            other_fish.x += 5

        if self.y > other_fish.y:
            self.y += 5
            other_fish.y -= 5
        else:
            self.y -= 5
            other_fish.y += 5

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        other_fish.hitbox = pygame.Rect(other_fish.x, other_fish.y, other_fish.width, other_fish.height)
        

        

