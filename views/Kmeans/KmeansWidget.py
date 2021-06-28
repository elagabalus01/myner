from .Ui_KmeansWidget import Ui_KmeansWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
class KmeansWidget(QWidget,Ui_KmeansWidget):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
