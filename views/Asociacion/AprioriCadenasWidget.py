from .Ui_AprioriCadenasWidget import Ui_AprioriCadenasWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
class AprioriCadenasWidget(QWidget,Ui_AprioriCadenasWidget):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
    
