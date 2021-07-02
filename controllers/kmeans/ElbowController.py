from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QThread
from .ClusterWorker import ClusterWorker

class ElbowController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=Canvas(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)
        self.view.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)
        self.elbow_thread=None
        self.elbow_worker=None

    def calcular_elbow(self):
        self.elbow_thread=QThread()
        self.elbow_worker=ClusterWorker(self.model)
        self.elbow_worker.moveToThread(self.elbow_thread)

        self.elbow_worker.complete.connect(self.elbow_thread.quit)
        self.elbow_worker.complete.connect(self.elbow_worker.deleteLater)
        self.elbow_thread.finished.connect(self.elbow_thread.deleteLater)

        self.elbow_thread.started.connect(self.elbow_worker.calcular_elbow)
        self.elbow_worker.complete.connect(self.plot)

        self.elbow_thread.start()

    def plot(self):
        SSE=self.model.SSE
        knee=self.model.knee_loc
        self.ax.cla()
        self.ax.clear()
        self.ax.plot(range(2, 12),SSE, marker='o')
        self.ax.set_xlabel('Cantidad de clusters *k*')
        self.ax.set_ylabel('SSE')
        self.ax.set_title('Elbow Method')
        self.ax.vlines(
            knee,SSE[0],SSE[9],
            linestyles="--", label="knee/elbow"
        )
        self.ax.legend(loc="best")
        self.graph.figure.canvas.draw()
        try:
            self.ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
