from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from TestHandView import Ui_TestHandWindow
import Globals
import random


class PlayTestWindow(QtWidgets.QMainWindow):
    aux = []
    curr_index = 0

    def __init__(self, parent=None):
        super(PlayTestWindow, self).__init__(parent)
        self.ui = Ui_TestHandWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.draw_hand)
        self.ui.pushButton_2.clicked.connect(self.draw_card)

    @pyqtSlot()
    def draw_hand(self):
        aux = list(Globals.deck.deck_list)
        random.shuffle(aux)
        self.ui.suggestionList.clear()
        self.ui.suggestionList.addItems(aux[:5])
        PlayTestWindow.curr_index = 4
        PlayTestWindow.aux = aux

    @pyqtSlot()
    def draw_card(self):
        PlayTestWindow.curr_index += 1
        if PlayTestWindow.curr_index >= Globals.deck.get_count():
            print("No more cards in deck")
        else:
            self.ui.suggestionList.addItem(PlayTestWindow.aux[PlayTestWindow.curr_index])
