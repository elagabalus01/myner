from .Ui_ElbowWidget import Ui_ElbowWidget
from PyQt5.QtWidgets import QWidget
class ElbowWidget(QWidget,Ui_ElbowWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)