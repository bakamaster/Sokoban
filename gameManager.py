from classes import EmptyTile, Box, Player, Switch

"""
Implementation of game manager class which handles player movement.
Key features:
    -Methods choose coorect movement option based on dictionaries
    -Class stores current state of the board
    -Class stores tiles that were changed in current movement
"""


class GameManager():
    def __init__(self, board: dict, numberOfSwitches, playerPosition):
        self._board = board
        self._numberOfSwitches = numberOfSwitches
        self._playerPosition = playerPosition
        self._tiles = {
            'empty tile': EmptyTile, 'box': Box,
            'player': Player, 'switch': Switch
        }
        self._movementType = {
            'empty tile': self.moveToEmptyTile, 'box': self.moveToBox,
            'switch': self.moveToSwitch, 'wall': self.moveToWall
        }
        self._tilesToUpdate = {}

    def board(self):
        return self._board

    def newBoard(self, newBoard):
        self._board = newBoard

    def newPlayerPosition(self, newPlayerPosition):
        self._playerPosition = newPlayerPosition

    def newNumberOfSwitches(self, newNumberOFSwitches):
        self._numberOfSwitches = newNumberOFSwitches

    def numberOfSwitches(self):
        return self._numberOfSwitches

    def resetTilesToUpdate(self):
        self._tilesToUpdate = {}

    def tilesToUpdate(self):
        return self._tilesToUpdate

    def positionAfterMovement(self, position, direction):
        return (position[0] + direction[0], position[1] + direction[1])

    def movePlayer(self, direction):
        """
        Basic movement method, used to move player.
        """
        positionAfterMovement = self.positionAfterMovement(
            self._playerPosition,
            direction
            )
        tileAfterMovement = str(self._board[positionAfterMovement])
        isOnSwitch = self._board[self._playerPosition].isOnSwitch()
        if self._movementType[tileAfterMovement]('player',
                                                 positionAfterMovement,
                                                 direction):
            if isOnSwitch:
                self._board[self._playerPosition] = Switch()
                self._tilesToUpdate[self._playerPosition] = Switch()
            else:
                self._board[self._playerPosition] = EmptyTile()
                self._tilesToUpdate[self._playerPosition] = EmptyTile()
            self._playerPosition = positionAfterMovement

    def moveToBox(self, tileType, startingBoxPosition, direction):
        """
        Method used when player or box needs to move
        to a tile that contains a box.
        """
        positionAfterMovement = self.positionAfterMovement(startingBoxPosition,
                                                           direction)
        tileAfterMovement = str(self._board[positionAfterMovement])
        if tileAfterMovement == 'box':
            return False
        isOnSwitch = self._board[startingBoxPosition].isOnSwitch()
        if self._movementType[tileAfterMovement]('box', positionAfterMovement,
                                                 direction):
            tile = self._tiles[tileType]()
            if isOnSwitch:
                self._numberOfSwitches += 1
                tile.changeIsOnSwitch()
            self._board[startingBoxPosition] = tile
            self._tilesToUpdate[startingBoxPosition] = tile
            return True

    def moveToWall(self, tileType, positionAfterMovement, direction):
        return False

    def moveToEmptyTile(self, tileType, positionAfterMovement, direction):
        tile = self._tiles[tileType]()
        self._board[positionAfterMovement] = tile
        self._tilesToUpdate[positionAfterMovement] = tile
        return True

    def moveToSwitch(self, tileType, positionAfterMovement, direction):
        tile = self._tiles[tileType]()
        tile.changeIsOnSwitch()
        self._board[positionAfterMovement] = tile
        if tileType == 'box':
            self._numberOfSwitches -= 1
        self._tilesToUpdate[positionAfterMovement] = tile
        return True
