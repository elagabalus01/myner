from PyQt5.QtCore import pyqtSignal,QObject

class ClusterWorker(QObject):
    complete = pyqtSignal()

    def __init__(self,model):
        super().__init__(parent=None)
        self.model=model

    def calcular_elbow(self):
        self.model.elbow()
        self.complete.emit()

    def calcular_clusters(self):
        self.model.calcular_clusters()
        self.model.calcular_centroides()
        self.model.set_colors()
        self.complete.emit()
