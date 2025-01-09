import json
from classes import classSelector
from errors import (LevelFileIncorrect, LevelFileNotFound,
                    LevelPermissionError, IncorrectBoard,
                    IncorrectNumberOfSwitches)

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
                    board[(coordinateX, coordinateY)] = classSelector(tile)
                    coordinateX += 1
                coordinateY += 1
        BoardCorrectionValidation(
            board,
            coordinateX-1,
            coordinateY-1,
            numberOfSwitches,
            numberOfBoxes
            )
    except FileNotFoundError:
        raise LevelFileNotFound(path)
    except PermissionError:
        raise LevelPermissionError()
    except json.JSONDecodeError:
        raise LevelFileIncorrect(path)
    except Exception as e:
        print(f'Unexpected exception {e}')

    return board, numberOfSwitches


def BoardCorrectionValidation(board: dict, maxX, maxY,
                              numberOfSwitches, numberOfBoxes,
                              showMessage=True):
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
    if numberOfSwitches <= 0 or numberOfBoxes != numberOfSwitches:
        raise IncorrectNumberOfSwitches(showMessage)
