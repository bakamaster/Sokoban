from errors import TileTypeError

"""
Implementation classes.
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


class Box(Tile):
    def __init__(self):
        super().__init__('yellow')
        self._isOnSwitch = False

    def isOnSwitch(self):
        return self._isOnSwitch

    def changeIsOnSwitch(self, state):
        self._isOnSwitch = state
        self._color = '#B8860B'

    def __str__(self):
        return 'box'


class Player(Tile):
    def __init__(self):
        super().__init__('green')
        self._isOnSwitch = False
        self._color = 'green'

    def getColor(self):
        return self._color

    def isOnSwitch(self):
        return self._isOnSwitch

    def changeIsOnSwitch(self, state):
        self._isOnSwitch = state
        self._color = 'darkgreen'

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
