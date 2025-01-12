from PySide6.QtWidgets import QMessageBox


class ErrorMessage(QMessageBox):
    def __init__(self, errorMessage: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setText(errorMessage)
        self.exec()


class LevelFileNotFound(Exception):
    def __init__(self, path):
        super().__init__(f'Level file not found, check the path {path}')
        if path != './testFile':
            ErrorMessage(f'Level file not found, check the path {path}')


class LevelPermissionError(Exception):
    def __init__(self):
        super().__init__("Could not load the level due to lacking permissions")
        ErrorMessage("Could not load the level due to lacking permissions")


class LevelFileIncorrect(Exception):
    def __init__(self, path):
        super().__init__("Level file is not in a corrct JSON format")
        if path != './testFile':
            ErrorMessage("Level file is not in a corrct JSON format")


class IncorrectBoard(Exception):
    def __init__(self, coordinates, showMessage=True):
        super().__init__(f'Board is incorrect, outer tiles are not walls,\
                          check tile {coordinates}')
        if showMessage:
            ErrorMessage("The board you were trying to load"
                         "has incorrect structure, it may not "
                         "work as intended!")


class IncorrectNumberOfSwitches(Exception):
    def __init__(self, showMessage=True):
        super().__init__('The board does have incorrect number of switches')
        if showMessage:
            ErrorMessage('The board does have incorrect number of switches')


class TileTypeError(Exception):
    def __init__(self, name, showMessage=True):
        super().__init__(f'Incorrect tile name- {name}')
        if showMessage:
            ErrorMessage("The board you were trying to load"
                         "has incorrect structure, it may not "
                         "work as intended!")


class MissingPlayerError(Exception):
    def __init__(self, showMessage=True):
        super().__init__('The player is missing')
        if showMessage:
            ErrorMessage("The player is missing from the board")
