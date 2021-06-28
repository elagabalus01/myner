from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator

class ElbowController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=Canvas(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)
        self.view.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)

    def calcular(self):
        SSE=[]
        #Se comprueba de 2 a 12 grupos
        for i in range(2,12):
            km=KMeans(n_clusters=i,random_state=0)
            km.fit(self.model.clean_data)
            SSE.append(km.inertia_)
        knee_loc=KneeLocator(range(2,12),SSE,curve='convex',direction='decreasing')
        self.ax.cla()
        self.ax.clear()
        self.ax.plot(range(2, 12), SSE, marker='o')
        self.ax.set_xlabel('Cantidad de clusters *k*')
        self.ax.set_ylabel('SSE')
        self.ax.set_title('Elbow Method')
        self.ax.vlines(
            knee_loc.knee,SSE[0],SSE[9],
            linestyles="--", label="knee/elbow"
        )
        self.ax.legend(loc="best")
        self.graph.figure.canvas.draw()
        try:
            self.ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
