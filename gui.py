from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from levelLoader import loadLevel
from ui_sokoban import Ui_MainWindow
import sys


class SokobanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._board = {}
        self._numberOfSwitches = 0
        self._currentLevel = 0
        self._levelpath = './level{levelNumber}.json'
        self.ui.resetLevel.triggered.connect(self.createBoard)
        self.ui.loadCustomLevel.triggered.connect(self.loadCustomLevel)
        self.clearBoard()
        self.loadLevelToBoard()

    def loadLevelToBoard(self, path=None):
        if path is None:
            path = self._levelpath.format(levelNumber=self._currentLevel)
        board, numberOfSwitches = loadLevel(path)
        self._board = board
        self._numberOfSwitches = numberOfSwitches
        self.createBoard()

    def clearBoard(self):
        self._boardLayout = QGridLayout(self.ui.frame)

    def createBoard(self):
        self.clearBoard()
        for (coordinateX, coordinteY), tile in self._board.items():
            tile = QLabel()
            if str(tile) == 'wall':
                tile.setStyleSheet('background-color: orange;')
            elif str(tile) == 'box':
                tile.setStyleSheet('background-color: yellow;')
            elif str(tile) == 'switch':
                tile.setStyleSheet('background-color: red;')
            elif str(tile) == 'player':
                tile.setStyleSheet('background-color: green;')
            elif str(tile) == 'empty tile':
                tile.setStyleSheet('background-color: white;')
            tile.setFixedSize(50, 50)
            self._boardLayout.addWidget(tile, coordinateX, coordinteY)

    def loadCustomLevel(self):
        pass

    def updateLevelInfo(self):
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')


def guiMain(args):
    app = QApplication(args)
    window = SokobanWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
