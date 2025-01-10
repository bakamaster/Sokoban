from classes import EmptyTile, Box, Player, Switch
from copy import deepcopy


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

    def numberOfSwitches(self):
        return self._numberOfSwitches

    def tilesToUpdate(self):
        tilesToUpdate = deepcopy(self._tilesToUpdate)
        self._tilesToUpdate = {}
        return tilesToUpdate

    def positionAfterMovement(position, direction):
        return (position[0] + direction[0], position[1] + direction[1])

    def movePlayer(self, direction):
        positionAfterMovement = self.positionAfterMovement(
            self._playerPosition,
            direction
            )
        tileAfterMovement = str(self._board[positionAfterMovement])
        isOnSwitch = self._board[self._playerPosition].isOnSwitch()
        if self._movementType[tileAfterMovement]('player',
                                                 self._playerPosition,
                                                 direction):
            if isOnSwitch:
                self._board[self._playerPosition] = Switch()
            else:
                self._board[self._playerPosition] = EmptyTile()
            self._tilesToUpdate[self._playerPosition] = Player()

    def moveToBox(self, tileType, startingBoxPosition, direction):
        positionAfterMovement = self.positionAfterMovement(startingBoxPosition,
                                                           direction)
        tileAfterMovement = str(self._board[positionAfterMovement])
        isOnSwitch = self._board[startingBoxPosition].isOnSwitch()
        if self._movementType[tileAfterMovement]('box', startingBoxPosition,
                                                 direction):
            self._board[startingBoxPosition] = self._tiles[tileType]()
            if isOnSwitch:
                self._board[startingBoxPosition].changeIsOnSwitch()
                if tileType == 'player':
                    self._numberOfSwitches += 1
            self._tilesToUpdate[positionAfterMovement] = (
                self._tiles[tileType]()
                )

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
        self._numberOfSwitches -= 1
        self._tilesToUpdate[positionAfterMovement] = tile
        return True
