from .Ui_ClustersWidget import Ui_ClustersWidget
from PyQt5.QtWidgets import QWidget
class ClustersWidget(QWidget,Ui_ClustersWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.splitter.setStretchFactor(0,9)
        self.splitter.setStretchFactor(1,1)