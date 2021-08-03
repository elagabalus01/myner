from .Ui_RegressionWidget import Ui_RegressionWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from views.infrastructure.Loadable import Loadable

class RegressionWidget(QWidget,Ui_RegressionWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
