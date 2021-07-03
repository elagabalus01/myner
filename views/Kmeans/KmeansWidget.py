from .Ui_KmeansWidget import Ui_KmeansWidget
from PyQt5.QtWidgets import QWidget
from views.infrastructure.Loadable import Loadable
class KmeansWidget(QWidget,Ui_KmeansWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
