# Defines the base class GameUnit
from pygame import Surface


class GameUnit:
    '''
    Base class for all game units
    '''
    def __init__(self, id):
        self.segments: list[GameUnitSegment] = []


class GameUnitSegment:
    '''
    Atomic unit segment which can be part of a larger unit

    Each segment has the following properties:

    name: the name of the unit
    id: the id of the unit
    max_hp: the maximum hit points of the unit
    current_hp: the current hit points of the unit
    atk: the attack points of the unit
    df: the defense points of the unit
    '''
    def __init__(self, name, id, max_hp, atk, df):
        # Properties
        self.name: str = name
        self.id: int = id
        self.max_hp: int = max_hp
        self.atk: int = atk
        self.df: int = df
        self.current_hp: int = max_hp

        self.image: Surface = None

        self.relative_position: tuple = (0, 0)
