from classes import EmptyTile, Box, Player, Switch
board = {}
numberOfSwitches = 0

"""
Implementation of player and box movement.
Key features:
    -Function that chooses movement option based on player beeing on switch
    -Function for movement in every scenario
"""


def positionAfterMovement(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def chooseMovementOption(position, direction, guiBoard, guiNumberOfSwitches):
    global board
    global numberOfSwitches
    board = guiBoard
    numberOfSwitches = guiNumberOfSwitches
    if board[position].isOnSwitch():
        if movePlayerFromSwitch(position, direction):
            board[position] = Switch()
    else:
        if movePlayerFromEmptySpace(position, direction):
            board[position] = EmptyTile()
    return board, numberOfSwitches


def movePlayerFromEmptySpace(position, direction):
    finalTile = positionAfterMovement(position, direction)
    if str(board[finalTile]) == 'empty tile':
        board[finalTile] = Player()
        return True
    elif str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            if moveBoxFromEmptyTile(finalTile, direction):
                board[finalTile] = Player()
                return True
        else:
            if moveBoxFromSwitch(finalTile, direction):
                board[finalTile] = Player()
                board[finalTile].changeIsOnSwitch(True)
                return True
    elif str(board[finalTile]) == 'switch':
        board[position] = EmptyTile()
        board[finalTile] = Player()
        board[finalTile].changeIsOnSwitch(True)
        return False


def moveBoxFromEmptyTile(originTile, direction):
    finalTile = positionAfterMovement(originTile, direction)
    global numberOfSwitches
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty tile':
        board[finalTile] = Box()
        return True
    elif str(board[finalTile]) == 'box':
        return moveBoxToBox(originTile, finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        numberOfSwitches -= 1
        board[originTile] = Player()
        board[finalTile] = Box()
        board[finalTile].changeIsOnSwitch(True)
        return True


def moveBoxToBox(originTile, finalTile, direction):
    global numberOfSwitches
    if not board[finalTile].isOnSwitch():
        if moveBoxFromEmptyTile(finalTile, direction):
            board[originTile] = Player()
            board[finalTile] = Box()
            return True
        else:
            return False
    else:
        if moveBoxFromSwitch(finalTile, direction):
            board[originTile] = Player()
            board[originTile].changeIsOnSwitch(True)
            board[finalTile] = Box()
            board[finalTile].changeIsOnSwitch(True)
            numberOfSwitches += 1
            return True
        else:
            return False


def movePlayerFromSwitch(position, direction):
    finalTile = positionAfterMovement(position, direction)
    if str(board[finalTile]) == 'empty tile':
        board[finalTile] = Player()
        return True
    elif str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'box':
        if not board[finalTile].isOnSwitch():
            if moveBoxFromEmptyTile(finalTile, direction):
                board[finalTile] = Player()
                return True
        else:
            if moveBoxFromSwitch(finalTile, direction):
                board[finalTile] = Player()
                board[finalTile].changeIsOnSwitch(True)
                return True
    elif str(board[finalTile]) == 'switch':
        board[finalTile] = Player()
        board[finalTile].changeIsOnSwitch(True)
        return True


def moveBoxToBoxWithSwitchChange(originTile, finalTile, direction):
    global numberOfSwitches
    if not board[finalTile].isOnSwitch():
        if moveBoxFromEmptyTile(finalTile, direction):
            board[finalTile] = Box()
            numberOfSwitches += 1
            board[originTile] = Player()
            board[originTile].changeIsOnSwitch(True)
            return True
        else:
            return False
    else:
        if moveBoxFromSwitch(finalTile, direction):
            numberOfSwitches += 1
            board[originTile] = Player()
            board[originTile].changeIsOnSwitch(True)
            board[finalTile] = Box()
            board[finalTile].changeIsOnSwitch(True)
            return True
        else:
            return False


def moveBoxFromSwitch(originTile, direction):
    global numberOfSwitches
    finalTile = positionAfterMovement(originTile, direction)
    if str(board[finalTile]) == 'wall':
        return False
    elif str(board[finalTile]) == 'empty tile':
        board[finalTile] = Box()
        numberOfSwitches += 1
        return True
    elif str(board[finalTile]) == 'box':
        return moveBoxToBoxWithSwitchChange(originTile, finalTile, direction)
    elif str(board[finalTile]) == 'switch':
        board[originTile] = Player()
        board[finalTile] = Box()
        board[finalTile].changeIsOnSwitch(True)
        return True
