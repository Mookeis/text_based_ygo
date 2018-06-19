# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 368)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 81, 16))
        self.label_2.setObjectName("label_2")
        self.addButton = QtWidgets.QPushButton(self.centralWidget)
        self.addButton.setGeometry(QtCore.QRect(170, 60, 113, 32))
        self.addButton.setObjectName("addButton")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(273, 30, 71, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.suggestionList = QtWidgets.QListWidget(self.centralWidget)
        self.suggestionList.setGeometry(QtCore.QRect(340, 30, 256, 261))
        self.suggestionList.setObjectName("suggestionList")
        self.deckList = QtWidgets.QListWidget(self.centralWidget)
        self.deckList.setGeometry(QtCore.QRect(20, 100, 261, 191))
        self.deckList.setObjectName("deckList")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_3.setObjectName("label_3")
        self.cardName = QtWidgets.QLineEdit(self.centralWidget)
        self.cardName.setGeometry(QtCore.QRect(20, 30, 261, 31))
        self.cardName.setObjectName("cardName")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Add card:"))
        self.label_2.setText(_translate("MainWindow", "Suggestions:"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Current Deck:"))
