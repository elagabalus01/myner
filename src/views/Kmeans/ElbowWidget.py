from .Ui_ElbowWidget import Ui_ElbowWidget
from PyQt5.QtWidgets import QWidget
from views.infrastructure.Loadable import Loadable
from views.infrastructure.CanvasWidget import CanvasWidget
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
class ElbowWidget(QWidget,Ui_ElbowWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_graph()

    def set_graph(self):
        self.graph=CanvasWidget(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)
        self.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)