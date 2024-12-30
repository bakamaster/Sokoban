from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QFileDialog
from ui_sokoban import Ui_MainWindow
from levelLoader import loadLevel
import sys


class SokobanWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._board = {}
        self._numberOfSwitches = 0
        self._currentLevel = 0
        self._customPath = None
        self._levelpath = './level{levelNumber}.json'
        self.ui.resetLevel.triggered.connect(self.createBoard)
        self.ui.loadCustomLevel.triggered.connect(self.loadCustomLevel)
        self.loadLevelToBoard()

    def loadLevelToBoard(self):
        if self._customPath is None:
            path = self._levelpath.format(levelNumber=self._currentLevel)
        board, numberOfSwitches = loadLevel(path)
        self._board = board
        self._numberOfSwitches = numberOfSwitches
        self.createBoard()

    def clearBoard(self):
        while self.ui.boardLayout.count():
            child = self.ui.boardLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def createBoard(self):
        for (coordinateX, coordinteY), tileType in self._board.items():
            tile = QLabel()
            tileType = str(tileType)
            if tileType == 'wall':
                tile.setStyleSheet('background-color: orange;')
            elif tileType == 'box':
                tile.setStyleSheet('background-color: yellow;')
            elif tileType == 'switch':
                tile.setStyleSheet('background-color: red;')
            elif tileType == 'player':
                tile.setStyleSheet('background-color: green;')
            elif tileType == 'empty tile':
                tile.setStyleSheet('background-color: white;')
            tile.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Expanding)
            self.ui.boardLayout.addWidget(tile, coordinateX, coordinteY)

    def loadCustomLevel(self):
        path, fileFilter = QFileDialog.getOpenFileName(self,
                                                       "Wybierz plik poziomu",
                                                       "Pliki JSON (*.json)")
        self._customPath = path

    def updateLevelInfo(self):
        self.ui.levelInfo.setText(f'Level {self._currentLevel+1}')


def guiMain(args):
    app = QApplication(args)
    window = SokobanWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
