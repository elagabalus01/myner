from .Ui_RegressionConfWidget import Ui_RegressionConfWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from views.infrastructure.Loadable import Loadable

class RegressionConfWidget(QWidget,Ui_RegressionConfWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
