from .Ui_PCA import Ui_PCA
from PyQt5.QtWidgets import QWidget
class PCA_Widget(QWidget,Ui_PCA):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)