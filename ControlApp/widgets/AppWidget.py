from .ui import ui_AppWidget
from PySide2 import QtWidgets


class AppWidget(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.ui = ui_AppWidget.Ui_MainWindow()
        self.ui.setupUi(self)
