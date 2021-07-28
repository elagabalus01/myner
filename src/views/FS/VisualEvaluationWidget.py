from PyQt5.QtWidgets import QWidget
from .Ui_VisualEvaluation import Ui_VisualEvaluation
from views.infrastructure.CanvasWidget import CanvasWidget
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
class VisualEvaluationWidget(QWidget,Ui_VisualEvaluation):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.add_graph()

    def add_graph(self):
        self.graph=None
        self.graph=CanvasWidget(Figure(),self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        # create an axes object in the figure
        self.axe=self.graph.figure.add_subplot(1, 1, 1)
        #ROW-COLUM
        self.scroll_grid.addWidget(self.graph,1,0,1,6,Qt.AlignHCenter)
