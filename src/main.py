import pygame
from fish import Fish

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    fish = Fish('fish1', 40, 5)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false
        
        screen.fill(("white"))
        
        fish.move()
        fish.draw(screen)


        pygame.display.flip()
        dt = clock.tick(30) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()  