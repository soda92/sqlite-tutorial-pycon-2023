from PySide2 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    from ..widgets.AppWidget import AppWidget

    window = AppWidget()
    window.show()
    sys.exit(app.exec_())
