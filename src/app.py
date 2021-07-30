import sys
from PyQt5.QtWidgets import QApplication
from controllers import MainController
import res.breeze_rc

from PyQt5 import QtCore
from matplotlib import use as matplotlib_bakend
matplotlib_bakend('Qt5Agg')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stream = QtCore.QFile(':/qbreeze/dark.qss')
    stream.open(QtCore.QIODevice.ReadOnly)
    app.setStyleSheet(QtCore.QTextStream(stream).readAll())
    win=MainController()
    win.run()
    sys.exit(app.exec())
