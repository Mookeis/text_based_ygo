import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot

import Globals
import TestHandViewController
from CreateDeckView import Ui_MainWindow
from YGOPricesAPI import YGOPricesAPI

card_list = YGOPricesAPI().get_names()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.testHandButton.clicked.connect(self.test_hand_clicked)
        self.ui.cardNameBox.textChanged.connect(self.search_text_changed)
        self.ui.suggestionList.itemDoubleClicked.connect(self.list_double_clicked)
        self.dialog = TestHandViewController.PlayTestWindow(self)
        self.ui.actionSave_Deck.triggered.connect(self.save_deck_triggered)
        self.ui.actionLoad_Deck.triggered.connect(self.load_deck_triggered)

    def update_lists(self, card):
        card_data = YGOPricesAPI().get_data(card)
        card_type = card_data.get("data").get("card_type")
        monster_type = card_data.get("data").get("type")
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        Globals.deck.deck_list.append(card)
        if (monster_type is not None and ("Link" in monster_type or "Xyz" in monster_type or
                                          "Synchro" in monster_type or "Fusion" in monster_type)):
            if Globals.extra.is_full():
                error_dialog.showMessage('Extra deck cannot exceed 15 cards')
                error_dialog.exec_()
            elif not Globals.extra.can_add_card(card):
                error_dialog.showMessage('Cannot add more than 3 copies of a card')
                error_dialog.exec_()
            else:
                Globals.extra.extra_list.append(card)
                self.ui.extraList.addItem(card)
                self.ui.extraCount.setValue(self.ui.extraCount.value() + 1)
        else:
            if Globals.deck.is_full():
                error_dialog.showMessage('Deck cannot exceed 60 cards')
                error_dialog.exec_()
            elif not Globals.deck.can_add_card(card):
                error_dialog.showMessage('Cannot add more than 3 copies of a card')
                error_dialog.exec_()
            else:
                if card_type == "monster":
                    self.ui.monsterList.addItem(card)
                    self.ui.monsterCount.setValue(self.ui.monsterCount.value() + 1)
                elif card_type == "spell":
                    self.ui.spellList.addItem(card)
                    self.ui.spellCount.setValue(self.ui.spellCount.value() + 1)
                elif card_type == "trap":
                    self.ui.trapList.addItem(card)
                    self.ui.trapCount.setValue(self.ui.trapCount.value() + 1)
                self.ui.totalCount.setValue(self.ui.totalCount.value() + 1)

    @pyqtSlot()
    def save_deck_triggered(self):
        deck_name = self.ui.deckNameBox.text()
        f = open(f"decks/{deck_name}.txt", "w")
        f.writelines("\n".join(Globals.deck.deck_list))
        f.close()

    @pyqtSlot()
    def load_deck_triggered(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        if filename[-4:] != ".txt":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.setWindowModality(QtCore.Qt.WindowModal)
            error_dialog.showMessage("Invalid File Type Selected")
            raise TypeError("Invalid File Type Selected")
        else:
            f = open(filename)
            for line in f.readlines():
                card = line.rstrip()
                Globals.deck.deck_list.append(card)
                self.update_lists(card)
            f.close()
            self.ui.deckNameBox.setText(filename.rsplit("/")[-1][:-4])

    @pyqtSlot()
    def test_hand_clicked(self):
        self.dialog.show()
        self.dialog.ui.deckList.addItems(Globals.deck.deck_list)

    @pyqtSlot()
    def search_text_changed(self):
        self.ui.suggestionList.clear()
        self.ui.suggestionList.addItems(list(filter(
            lambda k: self.ui.cardNameBox.text().lower() in k.lower(), card_list)))

    @pyqtSlot()
    def list_double_clicked(self):
        card = self.ui.suggestionList.currentItem().text()
        self.update_lists(card)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
