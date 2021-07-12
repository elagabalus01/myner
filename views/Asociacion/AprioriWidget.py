from .Ui_AprioriWidget import Ui_AprioriWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

class AprioriWidget(QWidget,Ui_AprioriWidget):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
