import json
import os
import pytest
from gameManager import chooseMovementOption
from classes import (EmptyTile, Box, Player, Wall,
                     Switch, classSelector, TileTypeError)
from levelLoader import (loadLevel, BoardCorrectionValidation,
                         IncorrectBoard, IncorrectNumberOfSwitches,
                         LevelFileIncorrect, LevelFileNotFound)


def testMovePlayerToEmptyTile():
    board = {(0, 0): Player(), (1, 0): EmptyTile(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board, numberOfSwitches = chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMovePlayerToSwitch():
    board = {(0, 0): Player(), (1, 0): Switch(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board, numberOfSwitches = chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()


def testMoveBoxToEmptyTile():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveBoxToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Switch(), (3, 0): EmptyTile()}
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(2, 0)].isOnSwitch()


def testMoveMultipleBoxesToEmptyTile():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): Box(), (3, 0): EmptyTile()}
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): Box()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveMultipleBoxesToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(), (2, 0): Box(), (3, 0): Switch()}
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): Box()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(3, 0)].isOnSwitch()


def testMovePlayerFromSwitch():
    board = {(0, 0): Player(), (1, 0): EmptyTile(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board[(0, 0)].changeIsOnSwitch(True)
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): Switch(), (1, 0): Player(),
                  (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )


def testMoveBoxFromSwitch():
    board = {(0, 0): Player(), (1, 0): Box(),
             (2, 0): EmptyTile(), (3, 0): EmptyTile()}
    board[(1, 0)].changeIsOnSwitch(True)
    chooseMovementOption((0, 0), (1, 0), board, 3)
    finalBoard = {(0, 0): EmptyTile(), (1, 0): Player(),
                  (2, 0): Box(), (3, 0): EmptyTile()}
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert board[(1, 0)].isOnSwitch()


def testLoadFromFile():
    testFilePath = './jsonTestFile'
    boardForFile = [["wall", "wall", "wall", "wall", "wall"],
                    ["wall", "emptyTile", "switch", "box", "wall"],
                    ["wall", "player", "emptyTile", "emptyTile", "wall"],
                    ["wall", "wall", "wall", "wall", "wall"]]
    with open(testFilePath, 'w') as fileHandle:
        json.dump(boardForFile, fileHandle)
    board, numberOfSwitches = loadLevel(testFilePath)
    finalBoard = {
        (0, 0): "wall", (1, 0): "wall", (2, 0): "wall",
        (3, 0): "wall", (4, 0): "wall",
        (0, 1): "wall", (1, 1): "empty tile", (2, 1): "switch",
        (3, 1): "box", (4, 1): "wall",
        (0, 2): "wall", (1, 2): "player", (2, 2): "empty tile",
        (3, 2): "empty tile", (4, 2): "wall",
        (0, 3): "wall", (1, 3): "wall", (2, 3): "wall",
        (3, 3): "wall", (4, 3): "wall"
        }
    assert (
        {coordinates: str(tile) for coordinates, tile in board.items()}
        == {coordinates: str(tile) for coordinates, tile in finalBoard.items()}
        )
    assert numberOfSwitches == 1
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
        BoardCorrectionValidation(board, 4, 3, 0, 2, showMessage=False)


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
        BoardCorrectionValidation(board, 4, 3, 0, 2, showMessage=False)


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
