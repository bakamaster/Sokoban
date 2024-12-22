class Tile:
    def __init__(self, coordinateX, coordinateY):
        self._coordinateX = coordinateX
        self._coordinateY = coordinateY

    def coordinateX(self):
        return self._coordinateX

    def coordinateY(self):
        return self._coordinateY


class NonMovableTile(Tile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)

    def isMovable(self):
        return False


class MovableTile(Tile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)

    def isMovable(self):
        return True


class Wall(NonMovableTile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)


class EmptyTile(Tile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)


class Switch(NonMovableTile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)
        self._isActive = False

    def isActive(self):
        return self._isActive

    def changeIsActive(self, state):
        self._isActive = state


class Box(MovableTile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)


class Player(MovableTile):
    def __init__(self, coordinateX, coordinateY):
        super().__init__(coordinateX, coordinateY)


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
