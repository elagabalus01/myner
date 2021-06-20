from PyQt5.QtWidgets import QWidget
from .Ui_FeatureSelectionWidget import Ui_FeatureSelectionWidget

class FeatureSelectionWidget(QWidget,Ui_FeatureSelectionWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
