from gamefield import GameField
from constants import BOARD_SIZE, CELL_SIZE
import pygame


class GameManager:
    '''
    Handles game logic and drawing the game field + UI
    '''

    def __init__(self, num_players=2, screen_width=1280, screen_height=720):
        gamefield_width = BOARD_SIZE * CELL_SIZE

        # Center the gamefields

        self.gamefields = [GameField(i, BOARD_SIZE,
                           ((screen_width/2 - gamefield_width)
                            // 2 + i*screen_width/2,
                            (screen_height - gamefield_width) // 2))
                           for i in range(num_players)]

    def draw(self, screen):
        # Render board
        for board in self.gamefields:
            surf = board.draw()
            screen.blit(surf, board.rect)
            pygame.display.update(board.rect)

        # Render UI
        pygame.font.init()

    def event(self, event):
        # check for mouse click
        event: pygame.event.Event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # find which field was clicked
            for board in self.gamefields:
                if board.rect.collidepoint(event.pos):
                    board.click(event.pos)
