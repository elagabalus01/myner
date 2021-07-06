from .Ui_EDA_Widget import Ui_EDA
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from views.infrastructure.CanvasWidget import CanvasWidget
from matplotlib.figure import Figure

class EDA_Widget(QWidget,Ui_EDA):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.add_graphs()
    
    def add_graphs(self):
        #Widget de histograma
        self.hist=CanvasWidget(Figure(figsize=(5,5)),self,
            width=5, height=4, dpi=100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.hist.setSizePolicy(sizePolicy)
        self.graph_layout.addWidget(self.hist,1,0,1,1,Qt.AlignHCenter)
        self.hist_ax=self.hist.figure.add_subplot(1, 1, 1)
        #Widget de caja de bigotes
        self.box=CanvasWidget(Figure(figsize=(5,5)),self,
            width=5, height=4, dpi=100)
        self.box.setSizePolicy(sizePolicy)
        self.graph_layout.addWidget(self.box,1,1,1,1,Qt.AlignHCenter)
        self.box_ax=self.box.figure.add_subplot(1, 1, 1)
        #Widget de caja de objectos
        self.obj=CanvasWidget(Figure(figsize=(7,5)),self,dpi=100)
        self.obj.setSizePolicy(sizePolicy)
        self.object_plot_grid.addWidget(self.obj,1,0,1,2,Qt.AlignHCenter)
        self.obj_ax=self.obj.figure.add_subplot(1, 1, 1)
