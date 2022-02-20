import pygame
from gamemanager import GameManager

# Initialize pygame
pygame.init()

pygame.display.set_caption("Dawn of Dominion")
screen = pygame.display.set_mode((1280, 720))
game = GameManager(2, 1280, 720)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        game.event(event)

    # Render chain
    screen.fill((0, 0, 0))
    game.draw(screen)

    pygame.time.delay(100)
