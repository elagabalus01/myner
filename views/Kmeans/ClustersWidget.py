from .Ui_ClustersWidget import Ui_ClustersWidget
from PyQt5.QtWidgets import QWidget
from views.infrastructure.Loadable import Loadable
from views.infrastructure.CanvasWidget import CanvasWidget
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy,QTableWidgetItem
class ClustersWidget(QWidget,Ui_ClustersWidget,Loadable):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.splitter.setStretchFactor(0,9)
        self.splitter.setStretchFactor(1,1)
        self.set_graph()

    def set_graph(self):
        self.graph=CanvasWidget(Figure(figsize=(10,5)))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 2, 1)
        self.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)
        self.ax_3d=self.graph.figure.add_subplot(1, 2, 2, projection='3d')
