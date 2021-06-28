from .Ui_Correlation import Ui_Correlation
from PyQt5.QtWidgets import QWidget

class CorrelationWidget(QWidget,Ui_Correlation):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

    
