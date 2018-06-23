# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handtest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 368)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.handLabel = QtWidgets.QLabel(self.centralWidget)
        self.handLabel.setGeometry(QtCore.QRect(340, 10, 81, 16))
        self.handLabel.setObjectName("handLabel")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(273, 30, 71, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.handList = QtWidgets.QListWidget(self.centralWidget)
        self.handList.setGeometry(QtCore.QRect(340, 30, 261, 121))
        self.handList.setObjectName("handList")
        self.deckList = QtWidgets.QListWidget(self.centralWidget)
        self.deckList.setGeometry(QtCore.QRect(20, 30, 261, 261))
        self.deckList.setObjectName("deckList")
        self.currentDeckLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentDeckLabel.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.currentDeckLabel.setObjectName("currentDeckLabel")
        self.drawHandButton = QtWidgets.QPushButton(self.centralWidget)
        self.drawHandButton.setGeometry(QtCore.QRect(340, 201, 113, 41))
        self.drawHandButton.setObjectName("drawHandButton")
        self.drawCardButton = QtWidgets.QPushButton(self.centralWidget)
        self.drawCardButton.setGeometry(QtCore.QRect(480, 201, 113, 41))
        self.drawCardButton.setObjectName("drawCardButton")
        self.currentDeckCount = QtWidgets.QSpinBox(self.centralWidget)
        self.currentDeckCount.setGeometry(QtCore.QRect(250, 10, 31, 21))
        self.currentDeckCount.setAlignment(QtCore.Qt.AlignCenter)
        self.currentDeckCount.setReadOnly(True)
        self.currentDeckCount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.currentDeckCount.setObjectName("currentDeckCount")
        self.handCount = QtWidgets.QSpinBox(self.centralWidget)
        self.handCount.setGeometry(QtCore.QRect(570, 10, 31, 21))
        self.handCount.setAlignment(QtCore.Qt.AlignCenter)
        self.handCount.setReadOnly(True)
        self.handCount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.handCount.setObjectName("handCount")
        self.backButton = QtWidgets.QPushButton(self.centralWidget)
        self.backButton.setGeometry(QtCore.QRect(410, 250, 113, 41))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 641, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hand Testing"))
        self.handLabel.setText(_translate("MainWindow", "Hand:"))
        self.currentDeckLabel.setText(_translate("MainWindow", "Current Deck:"))
        self.drawHandButton.setText(_translate("MainWindow", "Draw Hand"))
        self.drawCardButton.setText(_translate("MainWindow", "Draw Card"))
        self.backButton.setText(_translate("MainWindow", "Back"))
