from PyQt5.QtCore import QThread
from .ClusterWorker import ClusterWorker

class ElbowController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
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
        view=self.view
        view.graph.clear_axis(view.ax)
        view.ax.plot(range(2, 12),SSE, marker='o')
        view.ax.set_xlabel('Número de clusters')
        view.ax.set_ylabel('SSE')
        view.ax.set_title('Elbow Method')
        view.ax.vlines(
            knee,SSE[0],SSE[9],
            linestyles="--", label="knee/elbow"
        )
        view.ax.legend(loc="best")
        view.graph.update_axis(view.ax)
        view.loaded.emit(100)
