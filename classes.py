class NonMovableTile():
    def isMovable(self):
        return False


class MovableTile():
    def isMovable(self):
        return True


class Wall(NonMovableTile):
    def __str__(self):
        return 'wall'


class EmptyTile():
    def __str__(self):
        return 'empty tile'


class Switch(NonMovableTile):
    def __init__(self):
        self._isActive = False

    def __str__(self):
        return 'switch'

    def isActive(self):
        return self._isActive

    def changeIsActive(self, state):
        self._isActive = state


class Box(MovableTile):
    def __str__(self):
        return 'box'


class Player(MovableTile):
    def __str__(self):
        return 'player'


def classSelector(name, coordinateX, coordinateY):
    if name == 'wall':
        return Wall(coordinateX, coordinateY)
    elif name == 'emptyTile':
        return EmptyTile(coordinateX, coordinateY)
    elif name == 'switch':
        return Switch(coordinateX, coordinateY)
    elif name == 'box':
        return Box(coordinateX, coordinateY)
    elif name == 'player':
        return Player(coordinateX, coordinateY)
    else:
        pass
