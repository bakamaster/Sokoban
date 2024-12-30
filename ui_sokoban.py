# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sokoban.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 744)
        self.loadCustomLevel = QAction(MainWindow)
        self.loadCustomLevel.setObjectName(u"loadCustomLevel")
        self.resetLevel = QAction(MainWindow)
        self.resetLevel.setObjectName(u"resetLevel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.levelInfo = QLabel(self.centralwidget)
        self.levelInfo.setObjectName(u"levelInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.levelInfo.sizePolicy().hasHeightForWidth())
        self.levelInfo.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.levelInfo)

        self.moveInfo = QLabel(self.centralwidget)
        self.moveInfo.setObjectName(u"moveInfo")
        sizePolicy1.setHeightForWidth(self.moveInfo.sizePolicy().hasHeightForWidth())
        self.moveInfo.setSizePolicy(sizePolicy1)
        self.moveInfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.moveInfo)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.boardLayout = QGridLayout()
        self.boardLayout.setObjectName(u"boardLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.boardLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.boardLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1085, 20))
        self.menuLevel = QMenu(self.menubar)
        self.menuLevel.setObjectName(u"menuLevel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLevel.menuAction())
        self.menuLevel.addAction(self.loadCustomLevel)
        self.menuLevel.addAction(self.resetLevel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sokoban", None))
        self.loadCustomLevel.setText(QCoreApplication.translate("MainWindow", u"Load custom level", None))
        self.resetLevel.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.levelInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Level</span></p></body></html>", None))
        self.moveInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Use WSAD to move</span></p></body></html>", None))
        self.menuLevel.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
    # retranslateUi

