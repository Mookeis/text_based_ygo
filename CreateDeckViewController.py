from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from CreateDeckView import Ui_MainWindow
import sys
from YGOPricesAPI import YGOPricesAPI
import Levenshtein as lvst

card_list = YGOPricesAPI().get_names()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.lineEdit.textChanged.connect(self.text_changed)

    @pyqtSlot()
    def on_click(self):
        print()

    @pyqtSlot()
    def text_changed(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(list(filter(lambda k: self.ui.lineEdit.text() in k, card_list)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
