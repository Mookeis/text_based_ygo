import sys

from PyQt5 import QtWidgets

from CreateDeckViewController import CreateDeckWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(0)
    application = CreateDeckWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
