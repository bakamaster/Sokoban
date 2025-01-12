import json
from classes import classSelector
from errors import (LevelFileIncorrect, LevelFileNotFound,
                    LevelPermissionError, IncorrectBoard,
                    IncorrectNumberOfSwitches, MissingPlayerError,
                    MultiplePlayerError)

"""
Implementation of function that loads level from JSON file.
Key features:
    -Function that loads the level
    -Function that checks if level meets regulations
    -Custom errors for easier programe failure understanding
"""


def loadLevel(path):
    board = {}
    numberOfSwitches = 0
    coordinateY = 0
    numberOfBoxes = 0
    playerPosition = None
    try:
        with open(path, 'r') as fileHandle:
            data = json.load(fileHandle)
            for row in data:
                coordinateX = 0
                for tile in row:
                    if tile == 'switch':
                        numberOfSwitches += 1
                    elif tile == 'box':
                        numberOfBoxes += 1
                    elif tile == 'player':
                        playerPosition = (coordinateX, coordinateY)
                    board[(coordinateX, coordinateY)] = classSelector(tile)
                    coordinateX += 1
                coordinateY += 1
        boardCorrectionValidation(
            board,
            coordinateX-1,
            coordinateY-1,
            numberOfSwitches,
            numberOfBoxes,
            playerPosition
            )
    except FileNotFoundError:
        raise LevelFileNotFound(path)
    except PermissionError:
        raise LevelPermissionError()
    except json.JSONDecodeError:
        raise LevelFileIncorrect(path)
    except Exception as e:
        print(f'Unexpected exception {e}')

    return board, numberOfSwitches, playerPosition


def boardCorrectionValidation(board: dict, maxX, maxY,
                              numberOfSwitches, numberOfBoxes,
                              playerPosition,
                              showMessage=True):
    """
    Function which checks if board has correct number of switches/boxes and
    if all of the outer tiles are walls.
    """
    playerCounter = 0
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
            raise IncorrectBoard((coordinateX, coordinateY), showMessage)
        if tileType == 'player':
            playerCounter += 1
    if numberOfSwitches <= 0 or numberOfBoxes != numberOfSwitches:
        raise IncorrectNumberOfSwitches(showMessage)
    elif playerPosition is None:
        raise MissingPlayerError(showMessage)
    elif playerCounter > 1:
        raise MultiplePlayerError(showMessage)
