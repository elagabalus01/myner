from views import RegressionWidget,RegressionConfWidget,PredictionWidget
from model.infrastructure.observer import Observer
from .PredictionController import PredictionController
from .RegressionConfController import RegressionConfController
from .ClassifierWorker import ClassifierWorker
from model.Classifier import Classifier
class RegressionController(Observer):
    def __init__(self,model,view):
        super().__init__(model)
        self.model=model
        self.view=view
        self.classifier=Classifier(self.model)
        #Agregando widget de configuración
        self.conf=RegressionConfWidget(self.view)
        self.ctl_conf=RegressionConfController(self.model,self.conf,self.classifier)
        self.view.widget_list.addWidget(self.conf)
        #Agregando widget de predicción
        self.prediction=PredictionWidget(self.view)
        self.ctl_prediction=PredictionController(self.model,self.prediction,self.classifier)
        self.view.widget_list.addWidget(self.prediction)

        self.view.widget_list.setCurrentIndex(0)
        self.bind_signals()

    def bind_signals(self):
        self.conf.btn_calcular.pressed.connect(self.show_prediction)
        self.conf.btn_calcular.pressed.connect(self.ctl_prediction.set_dependiente)
        self.prediction.btn_conf.pressed.connect(self.show_conf)

    def show_conf(self):
        self.view.widget_list.setCurrentIndex(0)
        self.conf.scroll.verticalScrollBar().setValue(0)

    def show_prediction(self):
        self.view.widget_list.setCurrentIndex(1)
        self.prediction.scroll.verticalScrollBar().setValue(0)

    def end_loading(self,int):
        self.view.loaded.emit(40)

    def notify(self,model,*args,**kwargs):
        self.view.widget_list.setCurrentIndex(0) #Se debe recalcular el modelo
        if len(self.model.num_cols)>1 and len(self.model.objects)>0:
            self.ctl_conf.set_model()
            self.ctl_prediction.set_model()
            self.view.scrollArea.show()
        else:
            print("No tiene datos númericos")
            self.view.scrollArea.hide()
            self.end_loading(100)
