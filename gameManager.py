from classes import EmptyTile
board = {}


def moveToRight(coordinateX, coordinateY):
    originTile = board(coordinateX, coordinateY)
    if str(board[(coordinateX + 1, coordinateY)]) == 'empty space':
        board[(coordinateX + 1, coordinateY)] = originTile
        board[(coordinateX, coordinateY)] = EmptyTile()
