from classes import EmptyTile, Box, Player
board = {}


def movePlayer(coordinateX, coordinateY, direction):
    originTile = board[(coordinateX, coordinateY)]
    finalTile = (coordinateX + direction[0], coordinateY + direction[1])
    if str(board[finalTile]) == 'empty space':
        board[finalTile] = originTile
        board[(coordinateX, coordinateY)] = EmptyTile()
    elif str(board[finalTile]) == 'wall':
        pass
    elif str(board[finalTile]) == 'box':
        moveBox(finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        moveSwitch('player', finalTile, direction)


def moveBox(originTile, direction):
    finalTile = (originTile[0] + direction[0], originTile[1] + direction[1])
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty space':
        board[finalTile] = Box()
        board[originTile] = Player()
        return True
    elif str(board[finalTile]) == 'box':
        isMoved = moveBox(originTile, direction)
        if isMoved:
            board[finalTile] = Box()
            board[originTile] = Player()
    elif str(board[finalTile]) == 'switch':
        moveSwitch('box', finalTile, direction)


def moveSwitch(type, originTile, direction):
    pass
