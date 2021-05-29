from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog,
    QTableWidgetItem
)
from PyQt5 import QtCore
from views import Ui_main_window

class Window(QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
