import json
from classes import classSelector, TileTypeError


class LevelFileNotFound(Exception):
    def __init__(self, path):
        super().__init__(f'Level file not found, check the path {path}')


class LevelPermissionError(Exception):
    def __init__(self):
        super().__init__("Could not load the level due to lacking permissions")


class LevelFileIncorrect(Exception):
    def __init__(self):
        super().__init__("Level file is not in a corrct JSON format")


class IncorrectBoard(TileTypeError):
    def __init__(self, coordinates):
        super().__init__(f'Board is incorrect, outer tiles are not walls,\
                          check tile {coordinates}')


class IncorrctNumberOfSwitches(Exception):
    def __init__(self):
        super().__init__('The board does not have switches')


def loadLevel(path):
    board = {}
    numberOfSwitches = 0
    coordinateX = 0
    try:
        with open(path, 'r') as fileHandle:
            data = json.load(fileHandle)
            for row in data:
                coordinateY = 0
                for tile in row:
                    if tile == 'switch':
                        numberOfSwitches += 1
                    board[(coordinateX, coordinateY)] = classSelector(tile)
                    coordinateY += 1
                coordinateX += 1
        testBoardCorrection(
            board,
            coordinateX-1,
            coordinateY-1,
            numberOfSwitches
            )
    except FileNotFoundError:
        raise LevelFileNotFound(path)
    except PermissionError:
        raise LevelPermissionError()
    except json.JSONDecodeError:
        raise LevelFileIncorrect()
    except Exception as e:
        print(f'unexpected exception {e}')

    return board, numberOfSwitches


def testBoardCorrection(board: dict, maxX, maxY, numberOfSwitches):
    for (coordinateX, coordinateY), tile in board.items():
        tileType = str(tile)
        if (
            (
                coordinateX == 0
                or coordinateY == 0
                or coordinateX == maxX
                or coordinateY == maxY
                )
            and tileType != 'wall'
        ):
            raise IncorrectBoard((coordinateX, coordinateY))
    if numberOfSwitches <= 0:
        raise IncorrctNumberOfSwitches()
