from .Ui_KmeansWidget import Ui_KmeansWidget
from PyQt5.QtWidgets import QWidget
class KmeansWidget(QWidget,Ui_KmeansWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        