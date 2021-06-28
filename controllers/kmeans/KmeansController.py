from views import ElbowWidget,ClustersWidget
from model.infrastructure.observer import Observer
from .ElbowController import ElbowController
from .ClustersController import ClustersController
class KmeansController(Observer):
    def __init__(self,model,view):
        super().__init__(model)
        self.model=model
        self.view=view
        #Agregando widget del elbow method
        self.elbow=ElbowWidget(self.view)
        self.ctl_elbow=ElbowController(self.model,self.elbow)
        self.view.widget_list.addWidget(self.elbow)
        #Agregando widget de gráficas de cluster
        self.clusters=ClustersWidget(self.view)
        self.ctl_clusters=ClustersController(self.model,self.clusters)
        self.view.widget_list.addWidget(self.clusters)
        self.view.widget_list.setCurrentIndex(0)
        self.bind_signals()


    def bind_signals(self):
        self.elbow.btn_calcular.pressed.connect(self.show_kmeans)
        self.clusters.btn_elbow.pressed.connect(self.show_elbow)


    def show_kmeans(self):
        self.view.widget_list.setCurrentIndex(1)

    def show_elbow(self):
        self.view.widget_list.setCurrentIndex(0)

    def notify(self,model,*args,**kwargs):
        self.ctl_elbow.calcular()
        self.ctl_clusters.load_model()
        self.view.loaded.emit(40)
