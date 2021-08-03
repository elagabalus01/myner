from .Ui_PredictionWidget import Ui_PredictionWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from views.infrastructure.Loadable import Loadable

class PredictionWidget(QWidget,Ui_PredictionWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
