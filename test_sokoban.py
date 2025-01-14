import json
import os
import pytest
from gameManager import GameManager
from classes import (EmptyTile, Box, Player, Wall,
                     Switch, classSelector, TileTypeError)
from levelLoader import (loadLevel, boardCorrectionValidation,
                         IncorrectBoard, IncorrectNumberOfSwitches,
                         LevelFileIncorrect, LevelFileNotFound,
                         MissingPlayerError, MultiplePlayerError)


def testMovePlayerToEmptyTile():
    board = {(0, 0): Player(), (1, 0): EmptyTile(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in (
            gameManager.board().items()
            )}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMovePlayerToSwitch():
    board = {(0, 0): Player(), (1, 0): Switch(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in (
            gameManager.board().items()
            )}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()


def testMoveBoxToEmptyTile():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in (
            gameManager.board().items()
            )}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveBoxToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Switch(), (3, 0): EmptyTile()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in (
            gameManager.board().items()
            )}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(2, 0)].isOnSwitch()


def testMoveMultipleBoxesToEmptyTile():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Box(), (3, 0): EmptyTile()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Player(), (1, 0): Box(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in (
            gameManager.board().items()
            )}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveMultipleBoxesToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Box(), (3, 0): Switch()}
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Player(), (1, 0): Box(),
                  (2, 0): Box(), (3, 0): Switch()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMovePlayerFromSwitch():
    board = {(0, 0): Player(), (1, 0): EmptyTile(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board[(0, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Switch(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveBoxFromSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()
    assert gameManager.numberOfSwitches() == 1


def testMoveBoxFromSwitchToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Switch(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()
    assert board[(2, 0)].isOnSwitch()


def testMoveBoxAndPlayerFromSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch()
    board[(0, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 1, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Switch(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()
    assert gameManager.numberOfSwitches() == 2


def testMoveMultipleBoxesFromSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Box(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch()
    board[(2, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 0, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Player(), (1, 0): Box(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch() and board[(2, 0)].isOnSwitch()
    assert gameManager.numberOfSwitches() == 0


def testMoveMultipleBoxesAndPlayerFromSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Box(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch()
    board[(2, 0)].changeIsOnSwitch()
    board[(0, 0)].changeIsOnSwitch()
    gameManager = GameManager(board, 1, (0, 0))
    gameManager.movePlayer((1, 0))
    finalBoard = {(0, 0): Player(), (1, 0): Box(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    board = gameManager.board()
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert (
        board[(1, 0)].isOnSwitch() and
        board[(2, 0)].isOnSwitch() and
        board[(0, 0)].isOnSwitch()
        )
    assert gameManager.numberOfSwitches() == 1


def testLoadFromFile():
    testFilePath = './jsonTestFile'
    boardForFile = [["wall", "wall", "wall", "wall", "wall"],
                    ["wall", "emptyTile", "switch", "box", "wall"],
                    ["wall", "player", "emptyTile", "emptyTile", "wall"],
                    ["wall", "wall", "wall", "wall", "wall"]]
    with open(testFilePath, 'w') as fileHandle:
        json.dump(boardForFile, fileHandle)
    board, numberOfSwitches, playerPosition = loadLevel(testFilePath)
    finalBoard = {
        (0, 0): "wall", (1, 0): "wall", (2, 0): "wall",
        (3, 0): "wall", (4, 0): "wall",
        (0, 1): "wall", (1, 1): "emptyTile", (2, 1): "switch",
        (3, 1): "box", (4, 1): "wall",
        (0, 2): "wall", (1, 2): "player", (2, 2): "emptyTile",
        (3, 2): "emptyTile", (4, 2): "wall",
        (0, 3): "wall", (1, 3): "wall", (2, 3): "wall",
        (3, 3): "wall", (4, 3): "wall"
        }
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert numberOfSwitches == 1
    assert playerPosition == (1, 2)
    os.remove(testFilePath)


def testLoadBoardWithIncorrectTile():
    with pytest.raises(TileTypeError):
        classSelector('empty tile', showMessage=False)


def testBoardWithouSwitches():
    board = {
        (0, 0): Wall(), (1, 0): Wall(),
        (2, 0): Wall(), (3, 0): Wall(), (4, 0): Wall(),
        (0, 1): Wall(), (1, 1): EmptyTile(),
        (2, 1): Wall(), (3, 1): Box(), (4, 1): Wall(),
        (0, 2): Wall(), (1, 2): Player(),
        (2, 2): EmptyTile(), (3, 2): Box(), (4, 2): Wall(),
        (0, 3): Wall(), (1, 3): Wall(),
        (2, 3): Wall(), (3, 3): Wall(), (4, 3): Wall()
        }
    with pytest.raises(IncorrectNumberOfSwitches):
        boardCorrectionValidation(board, 4, 3, 0, 2, (1, 2), showMessage=False)


def testBoardWithouPlayer():
    board = {
        (0, 0): Wall(), (1, 0): Wall(),
        (2, 0): Wall(), (3, 0): Wall(), (4, 0): Wall(),
        (0, 1): Wall(), (1, 1): EmptyTile(),
        (2, 1): Wall(), (3, 1): Box(), (4, 1): Wall(),
        (0, 2): Wall(), (1, 2): Player(),
        (2, 2): EmptyTile(), (3, 2): Switch(), (4, 2): Wall(),
        (0, 3): Wall(), (1, 3): Wall(),
        (2, 3): Wall(), (3, 3): Wall(), (4, 3): Wall()
        }
    with pytest.raises(MissingPlayerError):
        boardCorrectionValidation(board, 4, 3, 1, 1, None, showMessage=False)


def testBoardWithMultiplePlayers():
    board = {
        (0, 0): Wall(), (1, 0): Wall(),
        (2, 0): Wall(), (3, 0): Wall(), (4, 0): Wall(),
        (0, 1): Wall(), (1, 1): Player(),
        (2, 1): Wall(), (3, 1): Box(), (4, 1): Wall(),
        (0, 2): Wall(), (1, 2): Player(),
        (2, 2): EmptyTile(), (3, 2): Switch(), (4, 2): Wall(),
        (0, 3): Wall(), (1, 3): Wall(),
        (2, 3): Wall(), (3, 3): Wall(), (4, 3): Wall()
        }
    with pytest.raises(MultiplePlayerError):
        boardCorrectionValidation(board, 4, 3, 1, 1, (1, 1), showMessage=False)


def testBoardWithoutWalls():
    board = {
        (0, 0): Wall(), (1, 0): Wall(),
        (2, 0): EmptyTile(), (3, 0): Wall(), (4, 0): Wall(),
        (0, 1): Wall(), (1, 1): EmptyTile(),
        (2, 1): Wall(), (3, 1): Box(), (4, 1): Wall(),
        (0, 2): Wall(), (1, 2): Player(),
        (2, 2): EmptyTile(), (3, 2): Box(), (4, 2): Wall(),
        (0, 3): Wall(), (1, 3): Wall(),
        (2, 3): Wall(), (3, 3): Wall(), (4, 3): Wall()
        }
    with pytest.raises(IncorrectBoard):
        boardCorrectionValidation(board, 4, 3, 1, 1, (1, 2), showMessage=False)


def testLoadNonExistentFile():
    with pytest.raises(LevelFileNotFound):
        loadLevel('./testFile')


def testLoadFileWithIncorrectFormat():
    path = './testFile'
    with open(path, 'w') as fileHandle:
        fileHandle.write('test')
    with pytest.raises(LevelFileIncorrect):
        loadLevel(path)
    os.remove(path)
