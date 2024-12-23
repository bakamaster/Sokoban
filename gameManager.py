from classes import EmptyTile
from levelLoader import loadLevel
board = {}


def move(coordinateX, coordinateY, direction):
    originTile = board[(coordinateX, coordinateY)]
    finaTile = (coordinateX + direction[0], coordinateY + direction[1])
    if str(board[finaTile]) == 'empty space':
        board[finaTile] = originTile
        board[(coordinateX, coordinateY)] = EmptyTile()
    elif not str(board[finaTile]) == 'wall':
        return False
    elif str(board[finaTile]) == 'box':
        if not move(finaTile[0], finaTile[1], direction):
            pass
        else:
            move(finaTile[0], finaTile[1], direction)
    elif str(board[finaTile]) == 'switch':
        if board[finaTile].isActive():
            pass
        else:
            board[finaTile] = originTile
