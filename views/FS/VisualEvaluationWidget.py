from PyQt5.QtWidgets import QWidget
from .Ui_VisualEvaluation import Ui_VisualEvaluation

class VisualEvaluationWidget(QWidget,Ui_VisualEvaluation):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
