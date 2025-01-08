from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PySide6.QtWidgets import QFileDialog, QMessageBox
from ui_sokoban import Ui_MainWindow
from copy import deepcopy
from levelLoader import loadLevel
from gameManager import chooseMovementOption
import sys
"""
Implementation of GUI using PySide6.
Script that provides graphical interface for Sokoban.
Key features:
    -Option to load a standard level or a one created by user
    -Option to restart the level
    -Ability to complete levels, go to the next one and complete the game
    -Handles player movement
"""


class SokobanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._board = {}
        self._originalBoard = {}
        self._numberOfSwitches = 0
        self._currentLevel = 0
        self._customPath = None
        self._levelpath = './level{levelNumber}.json'
        self._playerPosition = None
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')
        self.ui.resetLevel.triggered.connect(self.restartLevel)
        self.ui.loadCustomLevel.triggered.connect(self.loadCustomLevel)
        self.loadLevelToBoard()

    def loadLevelToBoard(self):
        # Function loads level from JSON file to the board
        if self._customPath is None:
            path = self._levelpath.format(levelNumber=self._currentLevel)
        else:
            path = self._customPath
        board, numberOfSwitches = loadLevel(path)
        self._board = board
        self._originalBoard = deepcopy(board)
        self._numberOfSwitches = numberOfSwitches
        self.createBoard()

    def restartLevel(self):
        # Function restarts level- changes board to the state
        # before any player movements
        self._board = deepcopy(self._originalBoard)
        self.createBoard()

    def clearBoard(self):
        # Function clears the board layout from any widgets
        while self.ui.boardLayout.count():
            child = self.ui.boardLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def createBoard(self):
        # Function creates graphical board 
        for (coordinateX, coordinateY), tileType in self._board.items():
            tile = QLabel()
            tile.setStyleSheet(f'background-color: {tileType.getColor()};')
            if str(tileType) == 'player':
                self._playerPosition = (coordinateX, coordinateY)
            tile.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Expanding)
            self.ui.boardLayout.addWidget(tile, coordinateY, coordinateX)

    def loadCustomLevel(self):
        path, fileFilter = QFileDialog.getOpenFileName(self,
                                                       "Wybierz plik poziomu",
                                                       "Pliki JSON (*.json)")
        self._customPath = path

    def updateLevelInfo(self):
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')

    def keyPressEvent(self, event):
        # Function handles keyboard input and moves player accordingly
        keyDirections = {
            Qt.Key.Key_W: (0, -1),
            Qt.Key.Key_A: (-1, 0),
            Qt.Key.Key_S: (0, 1),
            Qt.Key.Key_D: (1, 0)
            }
        if event.key() in keyDirections:
            self._board, self._numberOfSwitches = chooseMovementOption(
                self._playerPosition,
                keyDirections[event.key()],
                self._board,
                self._numberOfSwitches
                )
            self.createBoard()
            if self._numberOfSwitches == 0:
                self.newLevel()

    def newLevel(self):
        # Function loads new level and displays inforamtional window
        self.clearBoard()
        if self._customPath is None:
            self._currentLevel += 1
            self.updateLevelInfo()
            self.loadLevelToBoard()
        completedLevelDialog = QMessageBox()
        completedLevelDialog.setWindowTitle('Level completed')
        completedLevelDialog.setText(f'Congratulations!!! \
                                     You completed level {self._currentLevel}')
        completedLevelDialog.exec()

    def GameFinished():
        gameFinishedDialog = QMessageBox('Game completed')
        gameFinishedDialog.setText('Congratulations!!! \
                                   You completed the game')
        gameFinishedDialog.exec()


def guiMain(args):
    app = QApplication(args)
    window = SokobanWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
