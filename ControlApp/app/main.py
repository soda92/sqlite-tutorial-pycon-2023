from PySide2 import QtWidgets, QtCore
import sys

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    from ..widgets.AppWidget import AppWidget

    window = AppWidget()
    window.show()
    sys.exit(app.exec_())
