import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot

import Globals
from TestHandView import Ui_MainWindow


class PlayTestWindow(QtWidgets.QMainWindow):

    def __init__(self, parent):
        # Window set-up
        super(PlayTestWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI fills
        self.ui.deckList.addItems(Globals.deck.deck_list)
        self.ui.currentDeckCount.setValue(Globals.deck.get_count())

        # Create auxiliary deck list for random shuffling (preserves original)
        self.aux = list(Globals.deck.deck_list)
        # Index of current card place in deck list
        self.curr_index = 0

        # Connection Signals
        self.ui.drawHandButton.clicked.connect(self.draw_hand_clicked)
        self.ui.drawCardButton.clicked.connect(self.draw_card_clicked)
        self.ui.backButton.clicked.connect(self.back_clicked)

        # Error placeholder for error handling
        self.error_dialog = QtWidgets.QErrorMessage()
        # self.error_dialog.setWindowModality(QtCore.Qt.WindowModal)

        # Center frame to screen
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    @pyqtSlot()
    def draw_hand_clicked(self):
        random.shuffle(self.aux)
        self.ui.handList.clear()
        self.ui.handList.addItems(self.aux[:5])
        self.ui.handCount.setValue(5)
        self.curr_index = 5

    @pyqtSlot()
    def draw_card_clicked(self):
        if self.curr_index >= Globals.deck.get_count():
            self.error_dialog.showMessage("Unable to draw from empty deck")
            self.error_dialog.exec_()
        else:
            self.ui.handList.addItem(self.aux[self.curr_index])
            self.ui.handCount.setValue(self.ui.handCount.value() + 1)
            self.curr_index += 1

    @pyqtSlot()
    def back_clicked(self):
        self.close()
        self.parent().show()
