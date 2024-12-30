import json
from classes import classSelector


def loadLevel(path):
    board = {}
    numberOfSwitches = 0
    coordinateX = 0
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)
        for row in data:
            coordinateY = 0
            for tile in row:
                if tile == 'switch':
                    numberOfSwitches += 1
                board[(coordinateX, coordinateY)] = classSelector(tile)
                coordinateY += 1
            coordinateX += 1
    return board, numberOfSwitches
