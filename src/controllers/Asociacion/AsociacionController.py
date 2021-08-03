from model.infrastructure.observer import Observer
from .AprioriController import AprioriController
from views import AprioriWidget
class AsociacionController(Observer):
    def __init__(self,observable,view):
        super().__init__(observable)
        self.model=observable
        self.view=view
        # apriori_view=AprioriCadenasWidget()
        self.apriori_ctl=AprioriController(self.model,self.view)

    def notify(self,model,*args,**kwargs):
        self.apriori_ctl.set_model()
        # self.view.loaded.emit(10)
