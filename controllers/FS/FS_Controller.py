from views import VisualEvaluationWidget,CorrelationWidget,PCA_Widget
from .VisualEvaluationController import VisualEvaluationController
from .CorrelationController import CorrelationController
from .PCA_Controller import PCA_Controller
from model.infrastructure.observer import Observer
from PyQt5.QtWidgets import QCheckBox
from math import sqrt,floor

class FS_Controller(Observer):
    def __init__(self,model,view):
        super().__init__(model)
        self.model=model
        self.view=view
        #Visual selection widget
        self.visual=VisualEvaluationWidget(self.view)
        self.ctl_visual=VisualEvaluationController(self.model,self.visual)
        self.view.method.addWidget(self.visual)
        #Correlation widget
        self.corr=CorrelationWidget(self.view)
        self.ctl_corr=CorrelationController(self.model,self.corr)
        self.view.method.addWidget(self.corr)
        #PCA Widget
        self.pca=PCA_Widget(self.view)
        self.ctl_pca=PCA_Controller(self.model,self.pca)
        self.view.method.addWidget(self.pca)
        #DATOS INCIALES
        self.bind_signals()
        self.features_box=[]

    def bind_signals(self):
        self.view.method_box.activated.connect(self.set_current_method)
        self.view.btn_update_features.clicked.connect(self.update_features)

    def set_current_method(self,index):
        self.view.method.setCurrentIndex(index)

    def set_features(self):
        cols=len(self.model.numeric_columns())
        root=sqrt(cols)
        cols=floor(root)
        print(f"Número de features {cols}")
        i=0
        j=0
        for feature in self.model.numeric_columns():
            feature=QCheckBox(feature,self.view)
            feature.setTristate(0)
            feature.setCheckState(2)
            self.features_box.append(feature)
            print(f"Agregando en {feature.text()} {j,i}")
            self.view.feature_grid.addWidget(feature,j,i)
            i=i+1
            if i==cols+1:
                i=0
                j=j+1

    def update_features(self):
        filtered=[]
        for feature_checkbox in self.features_box:
            # print(f"{feature_checkbox.text()}:{feature_checkbox.checkState()}")
            if feature_checkbox.checkState()==0:
                print(f"Eliminado {feature_checkbox.text()}")
                filtered.append(feature_checkbox.text())

        self.model.filter_columns(filtered)
                # self.model.drop_list.append()
        # self.model.update()

    def notify(self,model,*args,**kwargs):
        if 'msg' in kwargs:
            if kwargs['msg']=='UPDATE':
                print("Es una actualización del modelo")
        else:
            self.set_features()
            self.ctl_visual.set_model()
            self.view.loaded.emit(10)
            self.ctl_corr.show_heatmap()
            self.view.loaded.emit(10)
            self.ctl_pca.set_model()
            self.view.loaded.emit(10)
