from gameManager import chooseMovementOption
from classes import EmptyTile, Box, Player, Switch


def testMoveMultipleBoxesToSwitch():
    board = {(0, 0): Player(), (1, 0): Box(), (2, 0): Box(), (3, 0): Switch()}
    chooseMovementOption((0, 0), (1, 0), board, 3)


testMoveMultipleBoxesToSwitch()
