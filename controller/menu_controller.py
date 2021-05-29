from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QKeySequence
from model import getDataFrame
class MenuController:
    def set_file_menu(self):
        self.actionAbrir.triggered.connect(self.openFile)
        self.actionAbrir.setShortcut(QKeySequence("Ctrl+o"))

        self.actionCerrar.triggered.connect(self.closeFile)
        self.actionCerrar.setShortcut(QKeySequence("Ctrl+w"))

        self.actionSalir.triggered.connect(self.exit)
        self.actionSalir.setShortcut(QKeySequence("Ctrl+q"))
