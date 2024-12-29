from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel
from levelLoader import loadLevel
import sys


class SokobanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._board = {}
        self._numberOfSwitches = 0
        self._currentLevel = 0
        self._levelpath = './level{levelNumber}.json'

    def loadLevelToBoard(self):
        levelPath = self._levelpath.format(self._currentLevel)
        board, numberOfSwitches = loadLevel(levelPath)
        self._board = board
        self._numberOfSwitches = numberOfSwitches
        self.createBoard()

    def updateLevelInfo(self):
        self.levelLabel.setText(f'Level {self._currentLevel+1}')

    def createBoard(self):
        pass


def guiMain(args):
    app = QApplication(args)
    window = SokobanWindow
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
