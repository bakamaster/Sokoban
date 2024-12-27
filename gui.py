from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel
from levelLoader import loadLevel
import sys


class SokobanUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self._board = {}
        self._numberOfSwitches = 0
        self._currentLevel = 0
        self._levelpath = './level{levelNumber}.json'
        self.initUI()

    def initUI(self):
        window = QWidget(self)
        centralLayout = QVBoxLayout(window)
        self.setWindowTitle('Sokoban')
        horizontalLayout = QHBoxLayout()
        levelLabel = QLabel(f'Level {self._currentLevel+1}', self)
        levelLabel.setAlignment(Qt.AlignLeft)
        horizontalLayout.addChildWidget(levelLabel)
        controlsLabel = QLabel('use WSAD to move and R to reset the level',
                               self)
        controlsLabel.setAlignment(Qt.AlignRight)
        horizontalLayout.addWidget(controlsLabel)
        centralLayout.addLayout(horizontalLayout)
        self.showFullScreen()

    def loadLevelToBoard(self):
        levelPath = self._levelpath.format(self._currentLevel)
        board, numberOfSwitches = loadLevel(levelPath)
        self._board = board
        self._numberOfSwitches = numberOfSwitches
        self.createBoard()

    def updateLevelInfo(self):
        self.level_label.setText(f'Level {self._currentLevel+1}')

    def createBoard(self):
        pass


def guiMain(args):
    app = QApplication(args)
    window = SokobanUI
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
