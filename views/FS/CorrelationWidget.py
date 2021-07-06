from .Ui_Correlation import Ui_Correlation
from PyQt5.QtWidgets import QWidget
from views.infrastructure.CanvasWidget import CanvasWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure

class CorrelationWidget(QWidget,Ui_Correlation):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.add_graph()

    def add_graph(self):
        self.graph=CanvasWidget(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.correlation_grid.addWidget(self.graph,1,0,1,1,Qt.AlignHCenter)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)

    
