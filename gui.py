from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QSizePolicy, QFileDialog, QMessageBox,
                               QListWidgetItem, QFrame)
from ui_sokoban import Ui_MainWindow
from copy import deepcopy
from classes import Player, Box, Switch, Wall, EmptyTile
from levelLoader import loadLevel
from gameManager import GameManager
import sys
"""
Implementation of GUI using PySide6.
Script that provides graphical interface for Sokoban.
Key features:
    -Option to load a standard level or a one created by user
    -Option to restart the level
    -Ability to complete levels, go to the next one and complete the game
    -Handles player movement
    -Only changed tiles are updated
"""


class SokobanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._originalBoard = {}
        self._originalNumberOfSwitches = 0
        self._currentLevel = 0
        self._gameManager = None
        self._customPath = None
        self._levelpath = './level{levelNumber}.json'
        self._playerPosition = None
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')
        self.ui.resetLevel.triggered.connect(self.restartLevel)
        self.ui.loadCustomLevel.triggered.connect(self.loadCustomLevel)
        startWindow()
        self.setFocus()
        self.initLegend()
        self.loadLevelToBoard()

    def initLegend(self):
        """
        Method that creates a legend, with names of tiles and
        their cooresponding colors.
        """
        player = Player()
        switch = Switch()
        wall = Wall()
        box = Box()
        emptyTile = EmptyTile()
        legend = {
            "wall": ("Wall", f"background-color: {wall.getColor()};"),
            "emptyTile": ("Empty Tile",
                          f"background-color: {emptyTile.getColor()};"),
            "player": ("Player", f"background-color: {player.getColor()};"),
            "box": ("Box", f"background-color: {box.getColor()};"),
            "switch": ("Switch", f"background-color: {switch.getColor()};"),
            "boxOnSwitch": ("Box located on switch",
                            f"background-color: {box.getColorOnSwitch()};"),
            "playerOnSwitch": (
                "Player located on switch",
                f"background-color: {player.getColorOnSwitch()};"
                )
        }
        options = [
            "To restart the level go to level menu or use ctrl+R",
            "To load custom level go to level menu or use ctrl+L",
            "Level menu is located in top left corner",
            "Your goal is to put all of the boxes on the switches",
            "You can move only one box at a time",
            "Player can step on empty tiles and switches",
            "You can only push boxes"
        ]
        self.setLegendTiles(legend)
        self.setLegendRules(options)

    def setLegendTiles(self, legend):
        for (description, color) in legend.values():
            legendItem = QListWidgetItem()
            legendWidget = QLabel(description)
            legendWidget.setStyleSheet(f'{color} font-size: 30px;')
            legendItem.setSizeHint(legendWidget.sizeHint())
            self.ui.legendList.addItem(legendItem)
            self.ui.legendList.setItemWidget(legendItem, legendWidget)

    def setLegendRules(self, options):
        maximumWidth = self.ui.legendLabel.maximumWidth()
        for option in options:
            legendItem = QListWidgetItem()
            legendWidget = QLabel(option)
            legendWidget.setMaximumWidth(maximumWidth)
            legendWidget.setWordWrap(True)
            legendWidget.setFrameStyle(QFrame.Box)
            legendWidget.setLineWidth(2)
            legendWidget.setStyleSheet('font-size: 20px;')
            legendItem.setSizeHint(legendWidget.sizeHint())
            self.ui.legendList.addItem(legendItem)
            self.ui.legendList.setItemWidget(legendItem, legendWidget)

    def loadLevelToBoard(self):
        """
        Method loads level from JSON file and creates game manager object
        """
        if self._customPath is None:
            path = self._levelpath.format(levelNumber=self._currentLevel)
        else:
            path = self._customPath
        board, numberOfSwitches, playerPosition = loadLevel(path)
        self._originalNumberOfSwitches = deepcopy(numberOfSwitches)
        self._originalBoard = deepcopy(board)
        self._originalPlayerPosition = deepcopy(playerPosition)
        self._gameManager = GameManager(
            board,
            numberOfSwitches,
            playerPosition
            )
        self.createBoard()

    def restartLevel(self):
        """
        Method restarts level- changes board to the state
        before any player movements
        """
        self._gameManager.newBoard(deepcopy(self._originalBoard))
        self._gameManager.newNumberOfSwitches(
            deepcopy(self._originalNumberOfSwitches)
            )
        self._gameManager.newPlayerPosition(
            deepcopy(self._originalPlayerPosition)
            )
        self.createBoard()

    def clearBoard(self):
        """
        Method clears the board layout from any widgets
        """
        while self.ui.boardLayout.count():
            child = self.ui.boardLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def createBoard(self):
        """
        Method creates graphical board
        """
        for (coordinateX, coordinateY), tileType in (
            self._gameManager.board().items()
        ):
            tile = QLabel()
            tile.setStyleSheet(f'background-color: {tileType.getColor()};')
            tile.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Expanding)
            self.ui.boardLayout.addWidget(tile, coordinateY, coordinateX)

    def loadCustomLevel(self):
        path, fileFilter = QFileDialog.getOpenFileName(self,
                                                       "Wybierz plik poziomu",
                                                       "Pliki JSON (*.json)")
        self._customPath = path
        self.setFocus()
        self.clearBoard()
        self.loadLevelToBoard()

    def updateLevelInfo(self):
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')

    def keyPressEvent(self, event):
        """
        Method handles keyboard input and moves player accordingly
        """
        keyDirections = {
            Qt.Key.Key_W: (0, -1),
            Qt.Key.Key_A: (-1, 0),
            Qt.Key.Key_S: (0, 1),
            Qt.Key.Key_D: (1, 0)
            }
        if event.key() in keyDirections:
            self._gameManager.movePlayer(keyDirections[event.key()])
            self.updateBoard()
            QApplication.processEvents()
            if (
                self._gameManager.numberOfSwitches() == 0
            ):
                self.newLevel()

    def updateBoard(self):
        """
        Method which updates tiles, that were changed during movement, in GUI.
        """
        for (coordinateX, coordinateY), tileType in (
            self._gameManager.tilesToUpdate().items()
        ):
            tile = QLabel()
            tile.setStyleSheet(f'background-color: {tileType.getColor()};')
            if str(tileType) == 'player':
                self._playerPosition = (coordinateX, coordinateY)
            tile.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Expanding)
            self.ui.boardLayout.addWidget(tile, coordinateY, coordinateX)
        self._gameManager.resetTilesToUpdate()

    def newLevel(self):
        """
        Method loads new level and displays inforamtional window
        """
        self.clearBoard()
        if self._customPath is None:
            self._currentLevel += 1
            if self._currentLevel < 3:
                newLevelWindow(self._currentLevel)
                self.updateLevelInfo()
                self.loadLevelToBoard()
            else:
                self.GameFinished()
        else:
            self.GameFinished()
        self.setFocus()

    def GameFinished(self):
        if gameFinishedWindow():
            if self._customPath is None:
                self._currentLevel = 0
            self.loadLevelToBoard()
            self.updateLevelInfo()
        self.setFocus()

    def mousePressEvent(self, event):
        self.setFocus()


class newLevelWindow(QMessageBox):
    """
    Class used to create window after finishing a level.
    """
    def __init__(self, currentLevel, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Level completed')
        self.setText(
            "<div style='text-align: center;'>"
            'Congratulations!!!<br><br>'
            f'You have completed level {currentLevel}.'
            )
        self.exec()


class gameFinishedWindow(QMessageBox):
    """
    Class used to create a window after finishing the game.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Finished")
        self.setText(
            "<div style='text-align: center;'>"
            'Congratulations!!!<br><br>'
            'You have completed the game.<br><br>'
            'Do you want to start over?'
            )
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.restartLevelChoice()

    def restartLevelChoice(self):
        result = self.exec()
        return result == QMessageBox.Yes


class startWindow(QMessageBox):
    """
    Class used to create starting window of the game.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sokoban")
        self.setText(
            "<div style='text-align: center;'>"
            "Welcome to sokoban!!!<br><br>"
            "The game has 3 levels, but you can load a custom "
            "one using level menu in the top left corner.<br><br>"
            "You need to push all of the boxes to the switches.<br><br>"
            "Guide the character using WSAD.<br><br>"
            "Your goal is to put all of the boxes on the switches.<br><br>"
            "You can move only one box at a time.<br><br>"
            "Player can step on empty tiles and switches.<br><br>"
            "You can only push boxes.<br><br>"
            )
        self.exec()


def guiMain(args):
    app = QApplication(args)
    window = SokobanWindow()
    window.showMaximized()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)
