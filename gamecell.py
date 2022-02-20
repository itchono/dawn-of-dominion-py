from enums import Terrain
from gameunit import GameUnit
import constants
from pygame import Surface, Rect, mouse


class GameCell:
    '''
    This class represents a cell in the game field.

    The cell can be either empty, or contain a unit.
    The cell also has a terrain type.
    The cell's grid position is stored as a tuple.
    '''
    def __init__(self, terrain, location, parent, unit=None):
        self.terrain: Terrain = terrain
        self.location: "tuple(int)" = location
        self.gamefield = parent
        self.unit: GameUnit = unit
        self.obscured: bool = False  # whether or not the other player can see this cell

    def draw(self, surface: Surface):
        # Draw relative to the gameboard surface
        surface.fill(constants.TERRAIN_COLOURS[self.terrain.value], self.rect)

        if self.unit is not None and self.obscured is False:
            surface.blit(self.unit.image, self.rect)

        if self.absolute_rect.collidepoint(mouse.get_pos()):
            # Highlight the cell (make color lighter)
            surface.fill(constants.CELL_HIGHLIGHT_COLOUR, self.rect)

    def click(self):
        self.terrain = Terrain.FIRM_GROUND
        print("Clicked cell:", self.location, "on board", self.gamefield.id)

    @property
    def rect(self) -> Rect:
        '''
        Gets relative rectangle to the gameboard surface
        '''
        return Rect(self.location[0] * constants.CELL_SIZE,
                    self.location[1] * constants.CELL_SIZE,
                    constants.CELL_SIZE, constants.CELL_SIZE)

    @property
    def absolute_rect(self) -> Rect:
        '''
        Gets the absolute rectangle of the cell
        '''
        return self.rect.move(self.gamefield.position)
