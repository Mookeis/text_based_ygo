from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from CreateDeckView import Ui_MainWindow
from YGOPricesAPI import YGOPricesAPI
from Deck import Deck
import Levenshtein as lvst
import sys

card_list = YGOPricesAPI().get_names()
deck = Deck()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.on_click)
        self.ui.cardName.textChanged.connect(self.text_changed)
        self.ui.suggestionList.itemDoubleClicked.connect(self.list_double_clicked)

    @pyqtSlot()
    def on_click(self):
        print()

    @pyqtSlot()
    def text_changed(self):
        self.ui.suggestionList.clear()
        self.ui.suggestionList.addItems(list(filter(
            lambda k: self.ui.cardName.text().lower() in k.lower(), card_list)))

    @pyqtSlot()
    def list_double_clicked(self):
        card = self.ui.suggestionList.currentItem().text()
        if deck.is_full():
            print("Deck is full")
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Deck cannot exceed 60 cards')
        elif not deck.can_add_card(card):
            print("Cannot add more than 3 copies of a card")
        else:
            deck.deck_list.append(card)
            self.ui.deckList.clear()
            self.ui.deckList.addItems(deck.deck_list)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
