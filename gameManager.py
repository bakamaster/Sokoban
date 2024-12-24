from classes import EmptyTile, Box, Player
board = {}
numberOfSwitches = 0


def movePlayerFromEmptySpace(position, direction):
    originTile = board[(position[0], position[1])]
    finalTile = (position[0] + direction[0], position[1] + direction[1])
    if str(board[finalTile]) == 'empty space':
        board[finalTile] = originTile
        board[position[0], position[1]] = EmptyTile()
    elif str(board[finalTile]) == 'wall':
        pass
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            moveBoxFromEmptySpace(finalTile, direction)
        else:
            pass
    elif str(board[finalTile]) == 'switch':
        board[position[0], position[1]] = EmptyTile()
        board[finalTile] = Player()
        board[finalTile].changeIsOnSwitch(True)


def moveBoxFromEmptySpace(originTile, direction):
    finalTile = (originTile[0] + direction[0], originTile[1] + direction[1])
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty space':
        board[finalTile] = Box()
        board[originTile] = Player()
        return True
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            isMoved = moveBoxFromEmptySpace(originTile, direction)
            if isMoved:
                board[finalTile] = Box()
                board[originTile] = Player()
                return True
            else:
                return False
        else:
            pass
    elif str(board[finalTile]) == 'switch':
        numberOfSwitches += 1
        board[originTile] = Player()
        board[finalTile] = Box()
        board[finalTile].changeIsOnSwitch(True)


def moveToSwitch(type, originTile, direction):
    pass
