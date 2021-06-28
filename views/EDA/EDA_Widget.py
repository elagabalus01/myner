from .Ui_EDA_Widget import Ui_EDA
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
class EDA_Widget(QWidget,Ui_EDA):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
