import typing
from PySide2 import QtWidgets, QtCore

from .ui import ui_Tab1


class Tab1(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.ui = ui_Tab1.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.showMessage)

    def showMessage(self):
        text = self.ui.lineEdit.text()
        box = QtWidgets.QMessageBox()
        box.setWindowTitle("messge")
        box.setText(text)
        box.exec_()

