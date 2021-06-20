from views import VisualEvaluationWidget,CorrelationWidget
from .VisualEvaluationController import VisualEvaluationController
from .CorrelationController import CorrelationController
from model.infrastructure.observer import Observer
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
        
        self.bind_signals()
        print(self.view.method.count())

    def bind_signals(self):
        self.view.method_box.activated.connect(self.set_current_method)

    def set_current_method(self,index):
        self.view.method.setCurrentIndex(index)
    
    def notify(self,model,*args,**kwargs):
        print(f"Abriendo el modelo desde FS controller: {model}")
        self.ctl_visual.set_model()
        self.ctl_corr.show_heatmap()
        
        
