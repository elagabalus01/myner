from .Ui_LoadingScreen import Ui_LoadingScreen
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

class LoadingScreen(QDialog,Ui_LoadingScreen):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.setWindowFlags(Qt.Window|Qt.WindowTitleHint|Qt.CustomizeWindowHint)
