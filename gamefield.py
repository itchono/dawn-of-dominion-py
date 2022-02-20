from gamecell import GameCell
from constants import CELL_SIZE
from pygame import Surface, Rect
from map_generator import terrain_generator
from math import floor

class GameField:
    '''
    This class represents the game field.

    It stores a N x N grid of Cell objects.
    '''
    def __init__(self, id, size=20, position=(0, 0)):
        terrain_map = terrain_generator(size)

        self.id = id # id of the player
        
        self.cells = [
            [GameCell(terrain_map[i][j], (i, j), self) for j in range(size)]
            for i in range(size)]
        self.size = size
        self.position = position

    def get_cell(self, location):
        '''
        Returns the cell at the given location.
        '''
        return self.cells[location[0]][location[1]]

    def draw(self) -> Surface:
        boardsurface = Surface((self.size * CELL_SIZE, self.size * CELL_SIZE))
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].draw(boardsurface)
        return boardsurface

    def click(self, location):
        # find which cell was clicked
        indx = floor((location[0]-self.position[0]) / CELL_SIZE)
        indy = floor((location[1]-self.position[1]) / CELL_SIZE)
        self.cells[indx][indy].click()

    @property
    def rect(self) -> Rect:
        return Rect(self.position, (self.size * CELL_SIZE, self.size * CELL_SIZE))
