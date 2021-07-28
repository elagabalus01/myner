from model.infrastructure.observer import Observer
from .PreviewController import PreviewController
from .StructController import StructController
from .MissingController import MissingController
from .GraphController import GraphController
class EDA_Controller(Observer):
    def __init__(self,observable,view):
        super().__init__(observable)
        self.model=observable
        self.view=view
        self.preview=PreviewController(self.model,self.view)
        self.struct=StructController(self.model,self.view)
        self.missing=MissingController(self.model,self.view.missed_table)
        self.graph=GraphController(self.model,self.view)

    def notify(self,model,*args,**kwargs):
        print(f"Abriendo el modelo: {model.file}")
        self.preview.set_preview_table()
        self.view.loaded.emit(10)
        self.struct.set_struct_table()
        self.missing.set_missing_table()
        self.view.loaded.emit(10)
        self.graph.set_model()
        self.view.loaded.emit(10)
