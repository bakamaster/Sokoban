import json
from classes import classSelector


def loadLevel(path):
    board = {}
    numberOfSwitches = 0
    x = 0
    y = 0
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)
        for row in data:
            for tile in row:
                if tile == 'switch':
                    numberOfSwitches += 1
                board[(x, y)] = classSelector(tile, x, y)
                y += 1
            x += 1
    return board, numberOfSwitches
