from controllers.infrastructure.Canvas import Canvas
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
import seaborn as sns
import numpy as np
class CorrelationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=Canvas(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.view.correlation_grid.addWidget(self.graph,1,0,1,1,Qt.AlignHCenter)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)
        
        #Mask oculta los valores diferente de 0 mask=matriz_inferior
    
    def show_heatmap(self):
        
        # self.ax.set_xticklabels(self.ax.get_xticklabels(), rotation = -45)
        corr=self.model.data.corr()
        matriz_inferior=np.triu(corr) #np.tri[u|l] u=upper l=lower
        heatmap=sns.heatmap(corr,cmap='RdBu_r',annot=True,ax=self.ax,
            mask=matriz_inferior)
        # self.graph.figrue=heatmap.figure
        
