import enum


# Enum for terrain types
class Terrain(enum.Enum):
    '''
    Firm ground, Loose ground, Calm sea, Rough sea
    '''
    FIRM_GROUND = 0
    LOOSE_GROUND = 1
    MOUNTAINOUS = 2
    CALM_SEA = 3
    ROUGH_SEA = 4


# Enum for cell state
class CellState(enum.Enum):
    EMPTY = 0
    OCCUPIED = 1
    DESTROYED = 2
