import json
from classes import classSelector


def loadLevel(path):
    board = {}
    x = 0
    y = 0
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)
        for row in data:
            for tile in row:
                board[(x, y)] = classSelector(tile, x, y)
                y += 1
            x += 1
    return board
