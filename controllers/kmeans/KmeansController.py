from views import ElbowWidget,ClustersWidget
from model.infrastructure.observer import Observer
from .ElbowController import ElbowController
from .ClustersController import ClustersController
from model.Clusterer import Clusterer
class KmeansController(Observer):
    def __init__(self,model,view):
        super().__init__(model)
        self.model=model
        self.view=view
        #Agregando widget del elbow method
        self.elbow=ElbowWidget(self.view)
        self.cluster_model=Clusterer(self.model.clean_numeric_data)
        self.ctl_elbow=ElbowController(self.cluster_model,self.elbow)
        self.view.widget_list.addWidget(self.elbow)
        #Agregando widget de gráficas de cluster
        self.clusters=ClustersWidget(self.view)
        self.ctl_clusters=ClustersController(self.cluster_model,self.clusters)
        self.view.widget_list.addWidget(self.clusters)
        self.view.widget_list.setCurrentIndex(0)
        self.bind_signals()

    def bind_signals(self):
        self.elbow.btn_calcular.pressed.connect(self.show_kmeans)
        self.clusters.btn_elbow.pressed.connect(self.show_elbow)
        self.elbow.loaded.connect(self.end_loading)

    def show_kmeans(self):
        self.view.widget_list.setCurrentIndex(1)
        self.clusters.scroll_clusters.verticalScrollBar().setValue(0)

    def show_elbow(self):
        self.view.widget_list.setCurrentIndex(0)

    def end_loading(self,int):
        self.view.loaded.emit(40)

    def set_model(self):
        self.cluster_model.data=self.model.clean_numeric_data

    def notify(self,model,*args,**kwargs):
        if len(self.model.num_cols)>1:
            self.set_model()
            self.ctl_elbow.calcular_elbow()
            self.ctl_clusters.load_model()
            self.view.scrollArea.show()
        else:
            print("No tiene datos númericos")
            self.view.scrollArea.hide()
            self.end_loading(100)
