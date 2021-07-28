from PyQt5.QtWidgets import QWidget
from .Ui_FeatureSelectionWidget import Ui_FeatureSelectionWidget
from PyQt5.QtCore import pyqtSignal
class FeatureSelectionWidget(QWidget,Ui_FeatureSelectionWidget):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.splitter.setStretchFactor(0,7)
