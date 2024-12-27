from classes import EmptyTile, Box, Player, Switch
board = {}
numberOfSwitches = 0


def chooseMovementOption(position, direction):
    if board[position].isOnSwitch():
        movePlayerFromSwitch(position, direction)
    else:
        movePlayerFromEmptySpace(position, direction)


def movePlayerFromEmptySpace(position, direction):
    originTile = board[(position[0], position[1])]
    finalTile = (position[0] + direction[0], position[1] + direction[1])
    if str(board[finalTile]) == 'empty tile':
        board[finalTile] = originTile
        board[position[0], position[1]] = EmptyTile()
    elif str(board[finalTile]) == 'wall':
        pass
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            moveBoxFromEmptySpace(finalTile, direction)
        else:
            moveBoxFromSwitch(finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        board[position[0], position[1]] = EmptyTile()
        board[finalTile] = Player()
        board[finalTile].changeIsOnSwitch(True)


def moveBoxFromEmptySpace(originTile, direction):
    finalTile = (originTile[0] + direction[0], originTile[1] + direction[1])
    global numberOfSwitches
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty tile':
        moveBoxToEmptySpace(originTile, finalTile, False)
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            isMoved = moveBoxFromEmptySpace(originTile, direction)
            if isMoved:
                moveBoxToEmptySpace(originTile, finalTile, False)
            else:
                return False
        else:
            moveBoxFromSwitch(finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        numberOfSwitches += 1
        board[originTile] = Player()
        board[finalTile] = Box()
        board[finalTile].changeIsOnSwitch(True)


def movePlayerFromSwitch(position, direction):
    finalTile = (position[0] + direction[0], position[1] + direction[1])
    if str(board[finalTile]) == 'empty tile':
        board[finalTile] = Player()
        board[position] = Switch()
    elif str(board[finalTile]) == 'wall':
        pass
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            moveBoxFromEmptySpace(finalTile, direction)
            board[position] = Switch()
        else:
            moveBoxFromSwitch(finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        board[position] = Switch()
        board[finalTile] = Player()
        board[finalTile].changeIsOnSwitch(True)


def moveBoxFromSwitch(originTile, direction):
    global numberOfSwitches
    finalTile = (originTile[0] + direction[0], originTile[1] + direction[1])
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty tile':
        moveBoxToEmptySpace(originTile, finalTile, True)
        numberOfSwitches -= 1
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            isMoved = moveBoxFromEmptySpace(originTile, direction)
            if isMoved:
                moveBoxToEmptySpace(originTile, finalTile, True)
                numberOfSwitches -= 1
            else:
                return False
        else:
            moveBoxFromSwitch(finalTile, direction)
            numberOfSwitches -= 1
    elif str(board[finalTile]) == 'switch':
        numberOfSwitches += 1
        board[originTile] = Player()
        board[finalTile] = Box()
        board[finalTile].changeIsOnSwitch(True)


def moveBoxToEmptySpace(originTile, finalTile, isOnSwitch):
    board[finalTile] = Box()
    board[originTile] = Player()
    if isOnSwitch:
        board[originTile].changeIsOnSwitch(True)
    return True
