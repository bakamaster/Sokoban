from errors import TileTypeError

"""
Implementation of tile classes.
Key features:
    -Error that handles incorrect tile name in board
    -Classes for each tile
    -Fuction that selects class for tile
"""


class Tile():
    def __init__(self, color):
        self._color = color

    def getColor(self):
        return self._color


class TileThatCanBeOnSwitch(Tile):
    def __init__(self, color, colorOnSwitch):
        super().__init__(color)
        self._isOnSwitch = False
        self._colorOnSwitch = colorOnSwitch

    def getColorOnSwitch(self):
        return self._colorOnSwitch

    def isOnSwitch(self):
        return self._isOnSwitch

    def changeIsOnSwitch(self):
        self._isOnSwitch = True
        self._color = self._colorOnSwitch


class Wall(Tile):
    def __init__(self):
        super().__init__('orange')

    def __str__(self):
        return 'wall'


class EmptyTile(Tile):
    def __init__(self):
        super().__init__('white')

    def __str__(self):
        return 'empty tile'


class Switch(Tile):
    def __init__(self):
        super().__init__('red')

    def __str__(self):
        return 'switch'


class Box(TileThatCanBeOnSwitch):
    def __init__(self):
        super().__init__('yellow', '#B8860B')
        self._isOnSwitch = False

    def __str__(self):
        return 'box'


class Player(TileThatCanBeOnSwitch):
    def __init__(self):
        super().__init__('green', '#90EE90')
        self._isOnSwitch = False
        self._color = 'green'

    def __str__(self):
        return 'player'


def classSelector(name, showMessage=True):
    tileDictionary = {
        'wall': Wall(), 'emptyTile': EmptyTile(),
        'switch': Switch(), 'box': Box(), 'player': Player()
        }
    if name in tileDictionary.keys():
        return tileDictionary[name]
    else:
        raise TileTypeError(name, showMessage)
