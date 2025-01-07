from PySide6.QtWidgets import QMessageBox


class TileTypeError(Exception):
    def __init__(self, name):
        super().__init__(f'Incorrect tile name- {name}')
        errorDialog = QMessageBox()
        errorDialog.setWindowTitle("Incorrect Board")
        errorDialog.setText("The board you were trying to load has incorrect\
                             structure, it may not work as intended!")


class Wall():
    def __init__(self):
        self._color = 'orange'

    def getColor(self):
        return self._color

    def __str__(self):
        return 'wall'


class EmptyTile():
    def __init__(self):
        self._color = 'white'

    def getColor(self):
        return self._color

    def __str__(self):
        return 'empty tile'


class Switch():
    def __init__(self):
        self._color = 'red'

    def getColor(self):
        return self._color

    def __str__(self):
        return 'switch'


class Box():
    def __init__(self):
        super().__init__()
        self._isOnSwitch = False
        self._color = 'yellow'

    def getColor(self):
        return self._color

    def isOnSwitch(self):
        return self._isOnSwitch

    def changeIsOnSwitch(self, state):
        self._isOnSwitch = state
        self._color = '#B8860B'

    def __str__(self):
        return 'box'


class Player():
    def __init__(self):
        super().__init__()
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


def classSelector(name):
    if name == 'wall':
        return Wall()
    elif name == 'emptyTile':
        return EmptyTile()
    elif name == 'switch':
        return Switch()
    elif name == 'box':
        return Box()
    elif name == 'player':
        return Player()
    else:
        raise TileTypeError(name)
